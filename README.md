# Jack's BlueOS Extension Repo

A personal BlueOS extension catalog for Raspberry Pi 4 and Raspberry Pi 5.

The catalog follows the same format as the
[Blue Robotics extension repository](https://github.com/bluerobotics/BlueOS-Extensions-Repository).
GitHub Pages publishes `manifest.json`, while a scheduled workflow refreshes
Docker Hub tags and image labels every six hours.

## Add this catalog to BlueOS

Use this manifest URL in the BlueOS Extensions Manager:

```text
https://jackskellet.github.io/Jacks_BlueOS_Extension_Repo/manifest.json
```

## Repository structure

Each extension is registered under:

```text
repos/<publisher>/<extension>/metadata.json
repos/<publisher>/<extension>/extension_logo.png
repos/<publisher>/company_logo.png
```

The Docker image supplies version-specific BlueOS metadata through its image
labels. Only `linux/arm64/v8` images are published because BlueOS documents
Raspberry Pi 4 and newer boards as ARM64 targets.

## Automation

`.github/workflows/publish-manifest.yml` validates metadata, runs a pinned
revision of Blue Robotics' manifest generator, and deploys the result through
GitHub Pages. Configure these repository secrets to authenticate Docker Hub
lookups:

- `DOCKER_USERNAME`
- `DOCKER_PASSWORD` — a Docker Hub access token
