# Inspecting Git repository

## The Three Main States

| State | Location | Description | Method of inspection |
| --- | --- | --- | --- |
| Commited | .git directory | Stored in DB | *git log* *git show* *...* |
| Modified | Working directory | Changed | *git status* *git diff* |
| Staged | Staging area (.git/index) | Changed and marked for next commit to the DB | *git status* |

Staging area has many names:
* Index
* Cache
* Directory cache
* Current directory cache
* Staging area
* Staged files

## Revision

There are many ways to distinguish a specific commit from Git repository.

1. ***SHA*** (hash) - The [[wp>SHA-1]] algorithm is used to create a unique 40-byte hexadecimal string in many corners of git. The SHA (hash-object cat-file)
1. (refnames, refs)
1. ***Branch reference*** (heads) - Branches in Git are nothing more than pointers to the commit. Branch reference is a SHA value of the most recent commit and it is updated with each new commit added. (show rev-parse show-ref)
1. ***Tag reference*** - Similar to Branch reference but does not change with new commits. (git describe)
1. ***HEAD*** (***@***) - Note the capital letters. Points to the current commit. (git describe)
1. ***Other*** like FETCH_HEAD, MERGE_HEAD, CHERRY_PICK_HEAD, ORIG_HEAD
1. ***<refname>@{<date>}*** - For example *master@{yesterday}*, *HEAD@{5 minutes ago}*. Note: Date parsing is undocumented but the parser [code](https://github.com/git/git/blob/master/date.c) can be accessed on github.
1. ***<refname>@{n}*** - For example *master@{7}* returns 7th prior commit from master head.
1. ***<refname>@{-n}*** - For example *@{-2}* returns 2nd commit checked out before current one.
1. ***<branchname>@{upstream}*** *git rev-parse --symbolic-full-name @{u}*
1. ***<rev>^n***
1. ***<rev>~n***
1. more ...

### Walking the tree with *^* and *~*

```
A =      = A^0
B = A^   = A^1     = A~1
C = A^2  = A^2
D = A^^  = A^1^1   = A~2
E = B^2  = A^^2
F = B^3  = A^^3
G = A^^^ = A^1^1^1 = A~3
H = D^2  = B^^2    = A^^^2  = A~2^2
I = F^   = B^3^    = A^^3^
J = F^2  = B^3^2   = A^^3^2
```

### Tree

(idea taken from [here](https://www.kernel.org/pub/software/scm/git/docs/gitrevisions.html))

![alt](/projects/progit.svg)

## Range

1. *<rev>* - ancestors of commit revision
1. *^<rev>*
1. *<rev1>..<rev2>* - reachable from rev2 but exclude reachable from rev1 (none is HEAD)
1. *<rev1>...<rev2>* - reachable from either but not both (none is HEAD)
1. more ...

<http://stackoverflow.com/questions/7251477/what-are-the-differences-between-double-dot-and-triple-dot-in-git-dif>

## Reflog

"Log of references" - list of updates to the references

*git reflog*

## Diff

Show difference between working directory (or index if *--cached*) and commited.

## Merge-Base

## Debugging with Git

| | |
| --- | --- |
| *blame* | Line-by-line who last modified line |
| *grep* | Search files for given expression |
| *bisect* | Manually switch between commits until the one that introduces a chenge is found |


## References

* <https://github.com/MaciejKucia/git_tree>
* <http://gitref.org/inspect/>
* <https://www.atlassian.com/git/tutorials/inspecting-a-repository/>
* <https://www.kernel.org/pub/software/scm/git/docs/gitrevisions.html>
* <https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection>
* <https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History>
* <https://git-scm.com/book/en/v2/Git-Commands-Inspection-and-Comparison>
* <https://git-scm.com/book/en/v2/Git-Commands-Debugging>
* <http://www.sbf5.com/~cduan/technical/git/git-1.shtml>
* <http://web.mit.edu/nelhage/Public/git-slides-2009.pdf>
* <http://stackoverflow.com/questions/7251477/what-are-the-differences-between-double-dot-and-triple-dot-in-git-dif>
* <https://git-scm.com/docs/git-status>
* <https://git-scm.com/docs/git-log>
* <https://git-scm.com/docs/git-hash-object>
* <https://git-scm.com/docs/git-cat-file>
* <https://git-scm.com/docs/git-rev-parse>
* <https://git-scm.com/docs/git-reflog>
