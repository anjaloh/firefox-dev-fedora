%global             source_name firefox
%global             application_name firefox-dev

Name:               firefox-dev
Version:            94.0b8
Release:            1%{?dist}
Summary:            Firefox Developer Edition (formerly "Aurora") pre-beta Web browser

License:            MPLv1.1 or GPLv2+ or LGPLv2+
URL:                https://www.mozilla.org/en-US/firefox/developer/
Source0:            https://download-installer.cdn.mozilla.net/pub/devedition/releases/%{version}/linux-x86_64/en-US/firefox-%{version}.tar.bz2
Source1:            firefox-developer-edition.desktop

ExclusiveArch:      x86_64

Requires(post):     xdg-utils
Requires(post):     gtk-update-icon-cache

%description
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

Bugs related to this package should be reported at my GitHub project:
<https://github.com/AnjaloHettiarachchi/firefox-dev-rpm/>

%prep
%setup -q -n %{source_name}

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}{/opt/%{application_name},%{_bindir},%{_datadir}/applications}

%__cp -r * %{buildroot}/opt/%{application_name}

%__ln_s /opt/%{application_name}/firefox %{buildroot}%{_bindir}/%{application_name}

%__install -D -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications

%post
xdg-icon-resource install --novendor --size 128 /opt/firefox-dev/browser/chrome/icons/default/default128.png firefox-developer-edition
gtk-update-icon-cache -f -t /usr/share/icons/hicolor

%files
%{_datadir}/applications/firefox-developer-edition.desktop
%{_bindir}/%{application_name}
/opt/%{application_name}

%changelog
* Thu Oct 21 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 94.0b8
- Minor version upgrade

* Mon Oct 18 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 94.0b7
- Minor version upgrade

* Fri Oct 15 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 94.0b6
- Minor version upgrade

* Wed Oct 13 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 94.0b5
- Minor version upgrade

* Wed Oct 13 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 94.0b4
- Minor version upgrade

* Fri Oct 08 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 94.0b3
- Minor version upgrade

* Thu Oct 07 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 94.0b2
- Minor version upgrade

* Thu Oct 07 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 94.0b1
- Major version upgrade

* Tue Sep 28 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 93.0b9
- Minor version upgrade

* Thu Sep 23 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 93.0b8
- Minor version upgrade

* Tue Sep 21 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 93.0b7
- Minor version upgrade

* Fri Sep 17 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 93.0b6
- Minor version upgrade

* Thu Sep 16 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 93.0b5
- Minor version upgrade

* Sat Sep 11 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 93.0b4
- Minor version upgrade

* Sat Sep 11 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 93.0b3
- Minor version upgrade

* Thu Sep 09 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 93.0b2
- Minor version upgrade

* Thu Sep 09 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 93.0b1
- Major version upgrade

* Sat Aug 28 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 92.0b9
- Minor version upgrade

* Wed Aug 18 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 92.0b8
- Minor version upgrade

* Wed Aug 18 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 92.0b7
- Minor version upgrade

* Wed Aug 18 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 92.0b6
- Minor version upgrade

* Wed Aug 18 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 92.0b5
- Minor version upgrade

* Mon Aug 16 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 92.0b4
- Minor version upgrade

* Sat Aug 14 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 92.0b3
- Minor version upgrade

* Thu Aug 12 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 92.0b2
- Minor version upgrade

* Tue Aug 10 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 92.0b1
- Major version upgrade

* Wed Jul 28 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 91.0b9
- Minor version upgrade

* Wed Jul 28 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 91.0b8
- Minor version upgrade

* Mon Jul 26 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 91.0b7
- Minor version upgrade

* Fri Jul 23 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 91.0b6
- Minor version upgrade

* Thu Jul 22 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 91.0b5
- Minor version upgrade

* Thu Jul 22 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 91.0b4
- Minor version upgrade

* Fri Jul 16 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 91.0b3
- Minor version upgrade

* Wed Jul 14 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 91.0b2
- Minor version upgrade

* Wed Jul 14 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 91.0b1
- Major version upgrade

* Tue Jun 29 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 90.0b12
- Minor version upgrade

* Wed Jun 23 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 90.0b11
- Minor version upgrade

* Mon Jun 21 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 90.0b10
- Minor version upgrade

* Fri Jun 18 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 90.0b9
- Minor version upgrade

* Wed Jun 16 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 90.0b8
- Minor version upgrade

* Mon Jun 14 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 90.0b7
- Minor version upgrade

* Sat Jun 12 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 90.0b6
- Minor version upgrade

* Thu Jun 10 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 90.0b5
- Minor version upgrade

* Mon Jun 07 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 90.0b4
- Minor version upgrade

* Mon Jun 07 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 90.0b3
- Minor version upgrade

* Thu Jun 03 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 90.0b2
- Minor version upgrade

* Thu Jun 03 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 90.0b1
- Major version upgrade

* Sat May 22 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b15-1
- Minor version upgrade

* Sat May 22 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b14-1
- Minor version upgrade

* Mon May 17 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b13-1
- Minor version upgrade

* Fri May 14 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b12-1
- Minor version upgrade

* Wed May 12 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b11-1
- Minor version upgrade

* Wed May 12 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b10-1
- Minor version upgrade

* Sat May 8 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b9-1
- Minor version upgrade

* Sat May 8 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b8-1
- Minor version upgrade

* Sat May 8 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b7-1
- Minor version upgrade

* Sat May 8 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b6-1
- Minor version upgrade

* Sat May 8 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b5-1
- Minor version upgrade

* Sat May 8 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b4-1
- Minor version upgrade

* Sat Apr 24 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b3-1
- Minor version upgrade

* Thu Apr 22 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b2-1
- Minor version upgrade

* Thu Apr 22 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 89.0b1-1
- Major version upgrade

* Sun Apr 11 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 88.0b9-1
- Minor version upgrade

* Thu Apr 08 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 88.0b8-1
- Minor version upgrade

* Tue Apr 06 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 88.0b7-1
- Minor version upgrade

* Sat Apr 03 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 88.0b6-1
- Minor version upgrade

* Thu Apr 01 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 88.0b5-1
- Minor version upgrade

* Mon Mar 29 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 88.0b4-1
- Minor version upgrade

* Fri Mar 26 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 88.0b3-1
- Minor version upgrade

* Thu Mar 25 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 88.0b2-1
- Minor version upgrade

* Thu Mar 25 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 88.0b1-1
- Major version upgrade

* Fri Mar 12 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 87.0b9-1
- Minor version upgrade

* Wed Mar 10 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 87.0b8-1
- Minor version upgrade

* Fri Feb 19 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 86.0b8-1
- Initial build
