**【Web開発100本ノック】**



以下テーマ0の解答




**課題00.**

    $ git --version

git version 2.51.0.windows.2



**課題01.**

commit d00d7a5a67e202a811e218318154878cf6e57009

Author: Yama-ryo-qu

Date:   Tue Oct 7 11:03:17 2025 +0900



    Initial commit



**課題02.**

    $ ssh -T git@github.com

Hi Yama-ryo-qu! You've successfully authenticated, but GitHub does not provide shell access.



**課題03.**

    $ git remote -v

origin  https://github.com/Yama-ryo-qu/meeting\_100nock\_web (fetch)

origin  https://github.com/Yama-ryo-qu/meeting\_100nock\_web (push)


**課題04.**

    $ git log
    
commit 87be73e7f87f089894d26337021426d39f5ddbaa (HEAD -> main, origin/main)
Author: Yama-ryo-qu
Date:   Fri Oct 24 22:20:56 2025 +0900

Update README.md

commit fc6bebee9ef74cd66d5b5bacba6a2b8359973f98
Author: Yama-ryo-qu
Date:   Fri Oct 24 22:18:26 2025 +0900

課題途中経過20251024


**課題05.**

        $ git status

On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        package-lock.json

nothing added to commit but untracked files present (use "git add" to track)


        $ git status

On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

nothing added to commit but untracked files present (use "git add" to track)

 
        $ git add .gitignore

 
        $ git commit -m "Add .gitignore"

[main be9c272] Add .gitignore
 1 file changed, 54 insertions(+)
 create mode 100644 .gitignore

 
        $ git status

On branch main
nothing to commit, working tree clean





