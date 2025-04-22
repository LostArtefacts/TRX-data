# TRX asset offload repository

This repository contains the large media assets (images, music, installer
icons, etc.) for **TR1X** and **TR2X**, offloaded from the main codebase to
keep bundle sizes small and improve clone/download performance.


## Zipping ship directories

To create zip archives of each `ship` directory (e.g., `tr1/ship` and
`tr2/ship`), run:

```bash
python tools/zip_ship.py
```

This will produce `tr1.zip` and `tr2.zip` in the root of the repository,
containing the contents of each `ship` directory.
