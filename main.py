import sublime, sublime_plugin, re

class LoadSpecCommand(sublime_plugin.WindowCommand):
  def run(self):
    active_view = self.window.active_view()
    active_file = active_view.file_name()

    spec_file = active_file.replace("app", "spec").replace("assets", "")

    if ".js" in spec_file:
      spec_file = spec_file.replace(".js", "_spec.js")
    else:
      (row, col) = active_view.rowcol(active_view.sel()[0].begin())
      open_file = open(active_file, 'r')
      lines_so_far = 0
      last_method_seen = ""
      for line in open_file.readlines():
        lines_so_far += 1
        method_found = re.search(r"^\s*def ([^\(^\s]*)", line)
        if method_found:
          last_method_seen = method_found.group(1).strip()
          last_method_seen = last_method_seen.replace("?", "_predicate")
          last_method_seen = last_method_seen.replace("!", "_bang")
          last_method_seen = last_method_seen.replace("=", "_writer")
        if lines_so_far == row:
          break
      spec_file = spec_file.replace(".rb", "/" + last_method_seen + "_spec.rb")

    self.window.open_file(spec_file)
