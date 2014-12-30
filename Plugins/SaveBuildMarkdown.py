import sublime, sublime_plugin

class SaveBuildMarkdown(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command("build")
		self.window.run_command("save")
