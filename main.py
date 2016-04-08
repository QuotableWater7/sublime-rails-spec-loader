import sublime, sublime_plugin, re

class LoadSpecCommand(sublime_plugin.WindowCommand):
  def run(self):
    active_view = self.window.active_view()
    active_file = active_view.file_name()

    spec_file = active_file.replace("app/assets", "spec")

    if "js" in spec_file:
      spec_file = spec_file.replace(".js", "_spec.js")
    else:
      (row, col) = active_view.rowcol(active_view.sel()[0].begin())
      open_file = open(active_file, 'r')
      lines_so_far = 0
      last_method_seen = ""
      for line in open_file.readlines():
        lines_so_far += 1
        if "def" in line:
          last_method_seen = re.search(r"def ([^\(]*)", line).group(1).strip()
        if lines_so_far == row:
          break

      # if instance method:
      #   something_controller.rb -> something_controller/method_name.rb
      # else
      #   model.rb -> model/class_methods/method_name.rb
      spec_file = spec_file.replace(".rb", "/" + last_method_seen + "_spec.rb")
      spec_file = spec_file.replace("app", "spec")

    self.window.open_file(spec_file)
