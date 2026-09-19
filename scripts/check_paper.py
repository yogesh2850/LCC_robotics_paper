"""Static checks only; not a substitute for a LaTeX/BibTeX build."""
import hashlib
import json
from pathlib import Path
import re

PAPER = Path(__file__).resolve().parents[1]


def main():
    bib = (PAPER / "refs.bib").read_text()
    keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)", bib)
    assert len(keys) == len(set(keys)), "duplicate bibliography keys"
    for name in ("root.tex", "proposed_method.tex"):
        src = (PAPER / name).read_text()
        src = re.sub(r"(?<!\\)%[^\n]*", "", src)
        citations = {k.strip() for group in re.findall(r"\\cite\{([^}]+)\}", src) for k in group.split(",")}
        assert citations <= set(keys), (name, "missing citation", citations-set(keys))
        labels = re.findall(r"\\label\{([^}]+)\}", src)
        assert len(labels) == len(set(labels)), (name, "duplicate labels")
        refs = set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", src))
        assert refs <= set(labels), (name, "unresolved refs", refs-set(labels))
        for path in re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", src):
            assert (PAPER / path).is_file(), (name, "missing figure", path)
        stack = []
        for kind, env in re.findall(r"\\(begin|end)\{([^}]+)\}", src):
            if kind == "begin":
                stack.append(env)
            else:
                assert stack and stack.pop() == env, (name, "unbalanced environment", env)
        assert not stack, (name, stack)
        braces = 0
        for brace in re.findall(r"(?<!\\)[{}]", src):
            braces += 1 if brace == "{" else -1
            assert braces >= 0, (name, "closing brace without opening")
        assert braces == 0, (name, "unbalanced braces", braces)
        print(f"{name}: citations, refs, figures, environments, braces OK")
    manifest = json.loads((PAPER / "results/interaction_sources.sha256.json").read_text())
    for relative, expected in manifest.items():
        actual = hashlib.sha256((PAPER.parent / relative).read_bytes()).hexdigest()
        assert actual == expected, (relative, "source changed since audit")
    print(f"All {len(manifest)} audited source hashes unchanged (including both plant.py files).")
    print("Static checks passed. PDF compilation/page count/layout still require a TeX installation.")


if __name__ == "__main__":
    main()
