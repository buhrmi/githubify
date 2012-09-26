import sublime
import sublime_plugin
import subprocess
import os


class GithubifyCommand(sublime_plugin.TextCommand):

    def check_output(self, command, cwd):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, cwd=cwd)
        output, unused_err = process.communicate()
        retcode = process.poll()
        if retcode:
            cmd = command
            error = subprocess.CalledProcessError(retcode, cmd)
            error.output = output
            sublime.status_message('This file probably is not part of a Github repository')
            raise error
        return output

    def run(self, edit):
        absfile = self.view.file_name()

        if absfile == None:
            return

        cwd = os.path.dirname(absfile)
        git_root = self.check_output("git rev-parse --show-toplevel", cwd).strip()
        github_repo = self.check_output("git remote -v 2> /dev/null | grep github | awk '{ print $2 }' | sed -e 's/git@github.com:\\(.*\\).git/\\1/' | head -n 1", cwd).strip()
        branch = self.check_output("git branch | sed -e '/^[^*]/d' -e 's/* \\(.*\)/\\1/' -e 's/#/%23/'", cwd).strip()
        relfile = os.path.relpath(absfile, git_root)

        sel = self.view.sel()[0]
        begin_line = self.view.rowcol(sel.begin())[0] + 1
        end_line = self.view.rowcol(sel.end())[0] + 1
        if begin_line == end_line:
            lines = begin_line
        else:
            lines = '%s-%s' % (begin_line, end_line)

        url = 'https://github.com/%s/blob/%s/%s#L%s' % \
            (github_repo, branch, relfile, lines)

        self.view.window().run_command('open_url', {"url": url})
