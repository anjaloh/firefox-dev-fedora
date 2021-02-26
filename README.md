# firefox-dev-fedora

<p align="center">
    <img width="368" height="68" src="https://www.mozilla.org/media/protocol/img/logos/firefox/browser/developer/logo-word-hor-lg.977a1e574948.png">
</p>
<p align="center">
    <img src="https://www.mozilla.org/media/img/firefox/developer/hero-screenshot.baf6dd693658.png">
</p>

An unofficial RPM package of [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/) designed for [Fedora](https://getfedora.org).

## Special Note

This is just a RPM packaging for the said software and does not include any licenses of its own. Only additional file included is the `.desktop` file written based on the original executable from the Firefox Release Channel (default).

## About the Application

This is a pre-beta release of Mozilla Firefox intended for Web developers and
enthusiasts who want early access to new features. It receives new updates
(almost) daily, adding and refining support for the very latest Web standards
that won't make it into the stable release of Firefox for some months. It also
comes with some addons for Web development enabled by default.

You may actually find that Developer Edition works just fine for normal everyday
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

2. Go to folder where the package downloaded and execute following command.

```Shell
# rpm -i firefox-dev-{version}.{dist}.rpm
```

3. Launch application from the Application Menu or execute, 
```Shell
$ firefox-dev
```