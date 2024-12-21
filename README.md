# Nwge Plugins for Bip

This repository contains plugins to aid development of [nwge] games using the
[Bip] build system. Each plugin is contained in its own directory with an
appropriate README explaining its purpose and use.

## Usage

1. Add this repository as a submodule in your Git repo.
    ```sh
    git submodule add https://github.com/nwge-games/nwge-plugins.git nwge-plugins
    ```
2. Use the plugin as `nwge-plugins/...`. For example, the `bundle` plugin would
   be used as `nwge-plugins/bundle`:
    ```toml
    [bundle]
    plug = "nwge-plugins/bundle"
    src = "source/data"
    out = "target/game.bndl"
    ```

We recommend structuring your project with a separate plugins directory to hold
your own plugins as well as other plugins. For example, to place all the nwge
plugins in the `plugins/nwge` directory:
```sh
git submodule add https://github.com/nwge-games/nwge-plugins.git plugins/nwge
```
And then to use the `bundle` plugin:
```toml
[bundle]
plug = "plugins/nwge/bundle"
src = "source/data"
out = "target/game.bndl"
```

[nwge]: https://qeaml.github.io/projects/nwge
[Bip]: https://codeberg.org/q/bip
