# sublime-rails-spec-loader
A plugin for sublime text that will open the spec for the file or method you are working on

### Usage:

The easiest approach is to set a key binding that runs the spec loading command.

1) Sublime Text -> Preferences -> Key Bindings - User

2) Add an entry for the new key binding:

```javascript
[
  {
    "keys": ["command+option+l"],
    "command": "load_spec"
  }
]
```

When in ruby code, running the command will open the spec for the method the cursor is currently located inside. When in javascript code, it'll open the spec for that file.
