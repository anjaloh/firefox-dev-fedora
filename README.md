# firefox-dev-fedora

<p align="center">
    <img src="https://res.cloudinary.com/axicon/image/upload/v1619083500/GitHub/AnjaloHettiarachchi/firefox-dev-fedora/github-og-template-01_q22uyi.jpg">
</p>

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/AnjaloHettiarachchi/firefox-dev-fedora) ![GitHub all releases](https://img.shields.io/github/downloads/AnjaloHettiarachchi/firefox-dev-fedora/total) [![Build & Release RPM & SRPM packages](https://github.com/AnjaloHettiarachchi/firefox-dev-fedora/actions/workflows/build_and_release.yml/badge.svg)](https://github.com/AnjaloHettiarachchi/firefox-dev-fedora/actions/workflows/build_and_release.yml)

An unofficial RPM package of [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/) designed for [Fedora](https://getfedora.org).

## Special Note

This is just an RPM packaging for the said software and does not include any licenses of its own. The only additional file included is the `.desktop` file written based on the original executable from the Firefox Release Channel (default).

## About the Application

This is a pre-beta release of Mozilla Firefox intended for Web developers and
enthusiasts who want early access to new features. It receives new updates
(almost) daily, adding and refining support for the very latest Web standards
that won't make it into the stable release of Firefox for some months. It also
comes with some addons for Web development enabled by default.

You may find that Developer Edition works just fine for everyday
use: Some users set it as their default Web browser. You can sign in to your
normal Firefox account and sync your preferences, extensions, and bookmarks,
etc. Or you can keep the Firefox versions separate, and use different profiles,
even different browser UI themes. Firefox Developer Edition can install
alongside the stable release of Firefox, making it easy to switch back and forth
between the two versions.

That being said, a lot of the technology here is still experimental, and there
will very likely be some bugs, so just remember that by using Developer Edition,
you're helping Mozilla make Firefox the best Web browser they can. And have fun!

Bugs related to Firefox Developer Edition should be reported directly to
Mozilla: <https://bugzilla.mozilla.org/>

## Installation

1. Download the latest RPM package built for your Fedora distribution from the release section.

2. Go to the folder where the package is downloaded and execute the following command.

```Shell
# To install/update ...
$ sudo dnf install firefox-dev-{version}-1.fc33.x86_64.rpm
```

3. Launch the application from the Application Menu or execute, 
```Shell
$ firefox-dev
```
