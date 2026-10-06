# Forge reference

The uploaded `forge-master.zip` is a snapshot of **Card-Forge/forge**, the third-party Magic: The Gathering rules engine.

It contains roughly 59,644 files and the uploaded archive is about 262 MB. Forge is licensed under **GPL-3.0**. It is intentionally **not vendored wholesale into EDH Sim**.

Upstream: https://github.com/Card-Forge/forge

## How EDH Sim should use Forge

Treat Forge as an external reference/dependency for studying rules-engine architecture, Commander support, and AI behavior. Keep EDH Sim's original source clearly separated unless we deliberately decide to derive/link GPL-covered code and accept the resulting licensing obligations.

The user's uploaded snapshot was inspected before this note was added; its root README identifies it as "Forge: The Magic: The Gathering Rules Engine" and its root LICENSE is GNU GPL v3.

If we later need a reproducible exact Forge revision, prefer recording an upstream commit SHA or using a Git submodule/fork rather than committing a 262 MB ZIP.
