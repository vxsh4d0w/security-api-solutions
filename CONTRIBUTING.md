# Contribute to the Microsoft Graph Security API samples and documentation

Thank you for your interest in the samples and documentation! We are opening up Microsoft Graph Security sample creation to all Microsoft Graph Security API integrators in the Microsoft Graph Security community. This includes samples and related content in various programming languages as per community needs. 


* [Ways to contribute](#ways-to-contribute)
* [Contribution Workflow](#contribution-workflow)
* [How to use Markdown to format your topic](#how-to-use-markdown-to-format-your-topic)
* [FAQ](#faq)
* [More resources](#more-resources)

## Ways to contribute

Here are some ways you can contribute to this: 

* To make small changes to an article [Contribute using GitHub](#contribute-using-github).
* To make changes to samples (involve code) or large changes for e.g., a new sample in a language it currently doesn't exist in [Contribution Workflow](#contribution-workflow).
* Report sample and documentation bugs via GitHub Issues
* Request new samples and documentation by filing GitHub Issues or by posting on the [tech community](https://techcommunity.microsoft.com/t5/Using-Microsoft-Graph-Security/bd-p/SecurityGraphAPI).
 

## Contribution Workflow

You can review the list of [Microsoft Graph Security samples repositories](sample-repos.md) to get familiarized with the availability of samples in different programmming languages as well as the state of each sample. 

We use and recommend the following workflow:

1. Create an issue for your work in the respective repo. 
    - Where to file the issue?
        - If you plan to contribute to an [existing sample](sample-repos.md), create an issue in the sample repo where you plan to contribute. 
        - If you plan to contribute a new sample or update documentation or if your change is not scoped to a certain [sample repo](sample-repos.md), [create an issue](https://github.com/microsoftgraph/security-api-solutions/issues/new) in this repo.  
    - Reuse an [existing issue](https://github.com/microsoftgraph/security-api-solutions/issues) on the topic, if there is one.
    - Get agreement from the team and the community that your proposed change is a good one.
    - Clearly state that you are going to take on implementing the sample, if that's the case. You can request that the issue be assigned to you. Note: The issue filer and the implementer don't have to be the same person.
    Note: If you are requesting to contribute a sample in a programming language for which a repo doesn't exist, we will first assign the issue to ourselves and set up a repo for that sample after which you can follow step #2 onwards to code and share the sample. 
2. Create a personal fork of the respective repository on GitHub (if you don't already have one). Refer to [Contribute using Git](#contribute-using-git) for details on joining the repo, etc.
3. Create a branch off of master (`git checkout -b mybranch`). 
    - Name the branch so that it clearly communicates your intentions, such as issue-123 or githubhandle-issue. 
    - Branches are useful since they isolate your changes from incoming changes from upstream. They also enable you to create multiple PRs from the same fork.
4. Make and commit your changes.
    - Please follow our [Commit Messages](contributing.md#commit-messages) guidance.
5. Avoid using proprietary terminology and generalize the samples as much as possible. Refer to the [C# sample](https://github.com/microsoftgraph/aspnet-security-api-sample) as a reference. 
6. Build the sample with your changes.
    - Make sure that the builds are clean.
    - Make sure that the sample works as expected on both Windows and Mac platforms.
7. Create a pull request (PR) against the upstream repository's **master** branch.
    - Push your changes to your fork on GitHub (if you haven't already).

Note: It is OK for your PR to include a large number of commits. Once your change is accepted, you will be asked to squash your commits into one or some appropriately small number of commits before your PR is merged.

Note: It is OK to create your PR as "[WIP]" (Work In Progress) on the upstream repo before the implementation is done. This can be useful if you'd like to start the feedback process concurrent with the sample implementation. State that this is the case in the initial PR comment.

### Contribute using GitHub

Use GitHub to contribute to this documentation without having to clone the repo to your desktop. This is the easiest way to create a pull request in this repository. Use this method to make a minor change that doesn't involve code changes. 

1. Once you are on the article in GitHub, sign in to GitHub (get a free account [Join GitHub](https://github.com/join)).
2. Choose the **pencil icon** (edit the file in your fork of this project) and make your changes in the **<>Edit file** window. 
3. Scroll to the bottom and enter a description.
4. Choose **Propose file change**>**Create pull request**.

You now have successfully submitted a pull request. Pull requests are typically reviewed within 10 business days. 

**Note** Using this method allows you to contribute to one article at a time.

### Contribute using Git

Use Git to contribute substantive changes, such as:

* Contributing code.
* Contributing changes that affect meaning.
* Contributing large changes to text.
* Adding new topics.

Here are details on how to do so:

1. If you don't have a GitHub account, set one up at [GitHub](https://github.com/join). 
2. After you have an account, install Git on your computer. Follow the steps in [Setting up Git Tutorial](https://help.github.com/articles/set-up-git/).
3. To submit a pull request using Git, follow the steps in [Use GitHub, Git, and this repository](#use-github-git-and-this-repository).
4. You will be asked to sign the Contributor's License Agreement if you are:

    * A member of the Microsoft Open Technologies group.
    * A contributor who doesn't work for Microsoft.

As a community member, you must sign the Contribution License Agreement (CLA) before you can contribute large submissions to a project. You only need to complete and submit the documentation once. Carefully review the document. You may be required to have your employer sign the document. For details, visit https://cla.microsoft.com.

Signing the CLA does not grant you rights to commit to the main repository, but it does mean that the Microsoft Graph Security team will be able to review and approve your contributions. You will be credited for your submissions.

Pull requests are typically reviewed within 10 business days.

### Use GitHub, Git, and this repository

**Note:** Most of the information in this section can be found in [GitHub Help] articles.  If you're familiar with Git and GitHub, skip to the **Contribute and edit content** section for the specifics of the code/content flow of this repository.

#### To set up your fork of the repository

If this is a sample you are creating for a language we do not have a sample for, please file an issue 
1.	Set up a GitHub account so you can contribute to this project. If you haven't done this, go to [GitHub](https://github.com/join) and do it now.
2.	Install Git on your computer. Follow the steps in the [Setting up Git Tutorial] [Set Up Git].
3.	Create your own fork of the respective sample (language) repository. To do this, go to the respective sample repo and at the top of the page,  choose the **Fork** button.
4.	Copy your fork to your computer. To do this, open Git Bash. At the command prompt enter:

        git clone https://github.com/<your user name>/<repo name>.git

    Next, create a reference to the root repository by entering these commands:

        cd <repo name>
        git remote add upstream https://github.com/microsoftgraph/<repo name>.git
        git fetch upstream

Congratulations! You've now set up your repository. You won't need to repeat these steps again.

#### Contribute and edit content

To make the contribution process as seamless as possible, follow these steps.

##### To contribute and edit content

1. Create a new branch.
2. Add new content or edit existing content.
3. Submit a pull request to the main repository.
4. Delete the branch.

**Important** Limit each branch to a single concept/article to streamline the work flow and reduce the chance of merge conflicts. Content appropriate for a new branch includes:

* A new article.
* Spelling and grammar edits.
* Applying a single formatting change across a large set of articles (for example, applying a new copyright footer).

##### To create a new branch

1.	Open Git Bash.
2.	At the Git Bash command prompt, type `git pull upstream master:<new branch name>`. This creates a new branch locally that is copied from the latest MicrosoftGraph master branch.
3.	At the Git Bash command prompt, type `git push origin <new branch name>`. This alerts GitHub to the new branch. You should now see the new branch in your fork of the repository on GitHub.
4.	At the Git Bash command prompt, type `git checkout <new branch name>` to switch to your new branch.

##### Add new content or edit existing content

You navigate to the repository on your computer by using File Explorer. The repository files are in `C:\Users\<yourusername>\<repo name>`.

To edit files, open them in an editor of your choice and modify them. To create a new file, use the editor of your choice and save the new file in the appropriate location in your local copy of the repository. While working, save your work frequently.

The files in `C:\Users\<yourusername>\<repo name>` are a working copy of the new branch that you created in your local repository. Changing anything in this folder doesn't affect the local repository until you commit a change. To commit a change to the local repository, type the following commands in GitBash:

    git add .
    git commit -v -a -m "<Describe the changes made in this commit>"

The `add` command adds your changes to a staging area in preparation for committing them to the repository. The period after the `add` command specifies that you want to stage all of the files that you added or modified, checking subfolders recursively. (If you don't want to commit all of the changes, you can add specific files. You can also undo a commit. For help, type `git add -help` or `git status`.)

The `commit` command applies the staged changes to the repository. The switch `-m` means you are providing the commit comment in the command line. The -v and -a switches can be omitted. The -v switch is for verbose output from the command, and -a does what you already did with the add command.

You can commit multiple times while you are doing your work, or you can commit once when you're done.

##### Submit a pull request to the main repository

When you're finished with your work and are ready to have it merged into the main repository, follow these steps.

##### To submit a pull request to the main repository

1.	In the Git Bash command prompt, type `git push origin <new branch name>`. In your local repository, `origin` refers to your GitHub repository that you cloned the local repository from. This command pushes the current state of your new branch, including all commits made in the previous steps, to your GitHub fork.
2.	On the GitHub site, navigate in your fork to the new branch.
3.	Choose the **Pull Request** button at the top of the page.
4.	Verify the Base branch is `microsoftgraph/<repo name>@master` and the Head branch is `<your username>/<repo name>@<branch name>`.
5.	Choose the **Update Commit Range** button.
6.	Add a title to your pull request, and describe all the changes you're making.
7.	Submit the pull request.

One of the site administrators will process your pull request. Your pull request will surface on the microsoftgraph/<repo name> site under Issues. When the pull request is accepted, the issue will be resolved.

##### Create a new branch after merge

After a branch is successfully merged (that is, your pull request is accepted), don't continue working in that local branch. This can lead to merge conflicts if you submit another pull request. To do another update, create a new local branch from the successfully merged upstream branch, and then delete your initial local branch.

For example, if your local branch X was successfully merged into the python-security-rest-sample master branch and you want to make additional updates to the content that was merged. Create a new local branch, X2, from the python-security-rest-sample master branch. To do this, open GitBash and execute the following commands:

    cd python-security-rest-sample
    git pull upstream master:X2
    git push origin X2

You now have local copies (in a new local branch) of the work that you submitted in branch X. The X2 branch also contains all the work other writers have merged, so if your work depends on others' work (for example, shared images), it is available in the new branch. You can verify that your previous work (and others' work) is in the branch by checking out the new branch...

    git checkout X2

...and verifying the content. (The `checkout` command updates the files in `C:\Users\<yourusername>\python-security-rest-sample` to the current state of the X2 branch.) Once you check out the new branch, you can make updates to the content and commit them as usual. However, to avoid working in the merged branch (X) by mistake, it's best to delete it (see the following **Delete a branch** section).

##### Delete a branch

Once your changes are successfully merged into the main repository, delete the branch you used because you no longer need it.  Any additional work should be done in a new branch.  

##### To delete a branch

1.	In the Git Bash command prompt, type `git checkout master`. This ensures that you aren't in the branch to be deleted (which isn't allowed).
2.	Next, at the command prompt, type `git branch -d <branch name>`. This deletes the branch on your computer only if it has been successfully merged to the upstream repository. (You can override this behavior with the `�D` flag, but first be sure you want to do this.)
3.	Finally, type `git push origin :<branch name>` at the command prompt (a space before the colon and no space after it).  This will delete the branch on your github fork.  


### Commit messages

Please format commit messages as follows (based on [A Note About Git Commit Messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)):

```
Summarize change in 50 characters or less

Provide more detail after the first line. Leave one blank line below the
summary and wrap all lines at 72 characters or less.

If the change fixes an issue, leave another blank line after the final
paragraph and indicate which issue is fixed in the specific format
below.

Fix #42.
```

### PR Feedback

Microsoft team and community members will provide feedback on your change. Community feedback is highly valued. You will often see the absence of team feedback if the community has already provided good review feedback. 

1 or more Microsoft team members will review every PR prior to merge. They will often reply with "LGTM, modulo comments". That means that the PR will be merged once the feedback is resolved. "LGTM" == "looks good to me".

There are lots of thoughts for how to efficiently discuss changes. It is best to be clear and explicit with your feedback. Please be patient with people who might not understand the finer details about your approach to feedback.


## How to use Markdown to format your topic

### Standard Markdown

All of the articles in this repository use Markdown.  While a complete introduction (and listing of all the syntax) can be found at [Markdown Home] [], we'll cover the basics you'll need.

If you're looking for a good editor, try [Visual Studio Code][vscode].

### Markdown basics

This is a list of the most common markdown syntax:

- **Line breaks vs. paragraphs:** In Markdown there is no HTML `<br />` element. Instead, a new paragraph is designated by an empty line between two blocks of text.
- **Italics:** The HTML `<i>some text</i>` is written `*some text*`
- **Bold:** The HTML `<strong>some text</strong>` element is written `**some text**`
- **Headings:** HTML headings are designated by an number of `#` characters at the start of the line.  The number of `#` characters corresponds to the hierarchical level of the heading (for example, `#` = h1, `##` = h2, and `###` = h3).
- **Numbered lists:** To create a numbered (ordered) list, start the line with `1. `. If you want multiple elements within a single list element, format your list as follows:

    1. Notice that there is a space after the '.'

       Now notice that there is a line break between the two paragraphs in the list element, and that the indentation here matches the indentation of the line above.

- **Bulleted lists:** Bulleted (unordered) lists are almost identical to ordered lists except that the `1. ` is replaced with either `- `, `* `, or `+ `.  Multiple element lists work the same way as they do with ordered lists.
- **Links:** The base syntax for a link is `[visible link text](link url)`.
  Links can also have references, which is discussed in the **Link and Image References** section below.
- **Images:** The base syntax for an image is `![alt text for the image](image url)`.
  Images can also have references, which is discussed in the **Link and Image References** section below.
- **In-line HTML:** Markdown allows you to include HTML inline, but this should be avoided.

### Link and image references

Markdown has a really nice feature that lets a user insert a reference instead of a URL for images and links.
Here is the syntax for using this feature:

```markdown
The image below is from [Google][googleweb]

![Google's logo][logo]

[googleweb]: http://www.google.com
[logo]: https://www.google.com/images/srpr/logo3w.png
```

By using references grouped at the bottom of your file, you can easily find, edit, and reuse link and image URLs.

### More resources

- For more information about Markdown, go to [their site][Markdown Home].
- For more information about using Git and GitHub, first check out the [GitHub Help section] [GitHub Help] and if necessary contact the site administrators.

[GitHub Home]: http://github.com
[GitHub Help]: http://help.github.com/
[Set Up Git]: http://help.github.com/win-set-up-git/
[Markdown Home]: http://daringfireball.net/projects/markdown/
[vscode]: https://code.visualstudio.com/

## FAQ

### How do I get a GitHub account?

Fill out the form at [Join GitHub](https://github.com/join) to open a free GitHub account. 

### Where do I get a Contributor's License Agreement? 

You will automatically be sent a notice that you need to sign the Contributor's License Agreement (CLA) if your pull request requires one. 

As a community member, **you must sign the Contribution License Agreement (CLA) before you can contribute large submissions to this project**. You only need complete and submit the documentation once. Carefully review the document. You may be required to have your employer sign the document.

### What happens with my contributions?

When you submit your changes, via a pull request, our team will be notified and will review your pull request. You will receive notifications about your pull request from GitHub; you may also be notified by someone from our team if we need more information. We reserve the right to edit your submission for legal, style, clarity, or other issues.
 
### Can I become an approver for this repository's GitHub pull requests?

Currently, we are not allowing external contributors to approve pull requests in [this](https://github.com/microsoftgraph/security-api-solutions) and other [Microsoft Graph Security samples repositories](sample-repos.md).

### How soon will I get a response about my change request or issue?

We typically review pull requests and respond to issues within 10 business days.

## More resources

* To learn more about Markdown, go to the Git creator's site [Daring Fireball].
* To learn more about using Git and GitHub, first check out the [GitHub Help section] [GitHub Help].

[GitHub Home]: http://github.com
[GitHub Help]: http://help.github.com/
[Set Up Git]: http://help.github.com/win-set-up-git/
[Markdown Home]: http://daringfireball.net/projects/markdown/
[Daring Fireball]: http://daringfireball.net/
