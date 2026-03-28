# TRX asset offload repository

This repository contains the large media assets (images, music, installer
icons, etc.) for **TRX**, offloaded from the main codebase to
keep bundle sizes small and improve clone/download performance.


## Zipping ship directories

To create zip archives of each `ship` directory (e.g., `tr1/ship` and
`tr2/ship`), run:

```bash
python tools/zip_ship
```

This keeps the legacy archives in the repository root for existing TR1X/TR2X
consumers, and also creates combined TRX archives under `trx/`, such as
`trx/tr1.zip`, `trx/tr1-ub.zip`, `trx/tr1-demo-pc.zip`, `trx/tr2.zip`,
`trx/tr2-gm.zip`, and `trx/tr3.zip`.
