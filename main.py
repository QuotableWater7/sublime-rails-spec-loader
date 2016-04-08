import sublime, sublime_plugin

class LoadSpecCommand(sublime_plugin.WindowCommand):
  def run(self):
    active_file = self.window.active_view().file_name()
    spec_file = active_file.replace("app/assets", "spec").replace(".js", "_spec.js")
    self.window.open_file(spec_file)
