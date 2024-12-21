# Bundle Plugin

This plugin will automatically create and update bundle files on every build.

## Usage

Example:

```toml
[bundle]
# The bundle plugin
plug = "plugins/nwge/bundle"
# Full path to source directory used to create the bundle
src = "source/data"
# Full path to destination bundle
out = "target/game.bndl"
# If you don't want to use the default `nwgebndl` tool, you can specify your own
# via the `exe` key:
#exe="make-nwge-bundle"
```
