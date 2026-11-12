#!/usr/bin/env python3
"""Check portable source and archive relocation; never install or access network."""
import argparse, hashlib, json, re, tempfile, zipfile
from pathlib import Path

def check(root):
 root=root.resolve();manifest=json.loads((root/'bundle.json').read_text());expected={'dashboard-discovery','dashboard-prototyping','dashboard-evaluation'}
 declared=manifest['skills'];assert len(declared)==3 and {Path(x).name for x in declared}==expected
 assert manifest['deployment_unit']=='whole-bundle-preserve-layout'
 skills=list(root.glob('skills/*/SKILL.md'));assert {p.parent.name for p in skills}==expected
 assert not any(p.is_symlink() for p in root.rglob('*')),'symlinks not portable'
 links=0
 for p in root.rglob('*.md'):
  for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
   if '://' in target or target.startswith('#'):continue
   assert not Path(target).is_absolute(),(p,target)
   dest=(p.parent/target.split('#')[0]).resolve();assert dest.is_relative_to(root),(p,target)
   assert dest.is_file(),(p,target);links+=1
 for p in skills:
  text=p.read_text();front=text.split('---',2)[1];fields=dict(line.split(': ',1) for line in front.strip().splitlines())
  assert set(fields)=={'name','description'} and fields['name']==p.parent.name
  assert len(text.splitlines())<500
 assert not list((root/'skills').rglob('references')),'maintain research once in shared root'
 return {'skills':sorted(expected),'markdown_links_checked':links,'shared_reference_files':len(list((root/'references').glob('*.md'))),'skill_words':{p.parent.name:len(p.read_text().split()) for p in skills}}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('bundle',type=Path);args=ap.parse_args();root=args.bundle.resolve();result=check(root)
 baseline={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file() and not any(x in {".git", "__pycache__"} for x in p.relative_to(root).parts)}
 with tempfile.TemporaryDirectory(prefix='dashboard-bundle-check-') as t:
  t=Path(t);archive=t/'bundle.zip'
  with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
   for name in baseline:z.write(root/name,name)
  relocated=t/'different-root'/'dashboard-workflow';relocated.mkdir(parents=True)
  with zipfile.ZipFile(archive) as z:z.extractall(relocated)
  assert check(relocated)==result
  assert baseline=={str(p.relative_to(relocated)):hashlib.sha256(p.read_bytes()).hexdigest() for p in relocated.rglob('*') if p.is_file()}
  (relocated/'references/workflow-contract.md').unlink()
  try:check(relocated)
  except (AssertionError,FileNotFoundError):missing_rejected=True
  else:raise AssertionError('missing shared dependency accepted')
 result.update(relocation_roundtrip='passed',byte_preservation='passed',missing_reference_negative='rejected',installation='not performed',behavior='not established by this check')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
