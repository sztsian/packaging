Name:           lxqt-l10n
Version:        0.13.0
Release:        1%{?dist}
Summary:        Translations for the LXQt desktop

License:        LGPLv2+
URL:            http://lxqt.org/
Source0:        https://github.com/lxde/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  pkgconfig(lxqt)
BuildRequires:  qt5-qttools-devel

# One should be able to pull in whole LXQt translation at once
# lximage-qt, obconf-qt and pavucontrol-qt are part of this package
# but no LXQt core applications, so they are not required here as users might
# not want to have these to be pulled in
Requires:       libfm-qt-l10n = %{version}-%{release}
Requires:       liblxqt-l10n = %{version}-%{release}
Requires:       lxqt-about-l10n = %{version}-%{release}
%if 0%{?fedora}
Requires:       lxqt-admin-l10n = %{version}-%{release}
%endif
Requires:       lxqt-config-l10n = %{version}-%{release}
Requires:       lxqt-globalkeys-l10n = %{version}-%{release}
Requires:       lxqt-notificationd-l10n = %{version}-%{release}
Requires:       lxqt-openssh-askpass-l10n = %{version}-%{release}
Requires:       lxqt-panel-l10n = %{version}-%{release}
Requires:       lxqt-policykit-l10n = %{version}-%{release}
Requires:       lxqt-powermanagement-l10n = %{version}-%{release}
Requires:       lxqt-runner-l10n = %{version}-%{release}
Requires:       lxqt-session-l10n = %{version}-%{release}
Requires:       lxqt-sudo-l10n = %{version}-%{release}
Requires:       pcmanfm-qt-l10n = %{version}-%{release}
Requires:       qterminal-l10n = %{version}-%{release}

%description
Translations for the LXQt desktop and its associated applications.

%package -n libfm-qt-l10n
Summary:        Translations for libfm-qt
Requires:       libfm-qt
%description -n libfm-qt-l10n
This package provides translations for the libfm-qt package.

%package -n liblxqt-l10n
Summary:        Translations for liblxqt
Requires:       liblxqt
%description -n liblxqt-l10n
This package provides translations for the liblxqt package.

%package -n lximage-qt-l10n
Summary:        Translations for lximage-qt
Requires:       lximage-qt
%description -n lximage-qt-l10n
This package provides translations for the lximage-qt package.

%package -n lxqt-about-l10n
Summary:        Translations for lxqt-about
Requires:       lxqt-about
%description -n lxqt-about-l10n
This package provides translations for the lxqt-about package.

%if 0%{?fedora}
%package -n lxqt-admin-l10n
Summary:        Translations for lxqt-admin
Requires:       lxqt-admin
%description -n lxqt-admin-l10n
This package provides translations for the lxqt-admin package.
%endif

%package -n lxqt-config-l10n
Summary:        Translations for lxqt-config
Requires:       lxqt-config
%description -n lxqt-config-l10n
This package provides translations for the lxqt-config package.

%package -n lxqt-globalkeys-l10n
Summary:        Translations for lxqt-globalkeys
Requires:       lxqt-globalkeys
%description -n lxqt-globalkeys-l10n
This package provides translations for the lxqt-globalkeys package.

%package -n lxqt-notificationd-l10n
Summary:        Translations for lxqt-notificationd
Requires:       lxqt-notificationd
%description -n lxqt-notificationd-l10n
This package provides translations for the lxqt-notificationd package.

%package -n lxqt-openssh-askpass-l10n
Summary:        Translations for lxqt-openssh-askpass
Requires:       lxqt-openssh-askpass
%description -n lxqt-openssh-askpass-l10n
This package provides translations for the lxqt-openssh-askpass package.

%package -n lxqt-panel-l10n
Summary:        Translations for lxqt-panel
Requires:       lxqt-panel
%description -n lxqt-panel-l10n
This package provides translations for the lxqt-panel package.

%package -n lxqt-policykit-l10n
Summary:        Translations for lxqt-policykit
Requires:       lxqt-policykit
%description -n lxqt-policykit-l10n
This package provides translations for the lxqt-policykit package.

%package -n lxqt-powermanagement-l10n
Summary:        Translations for lxqt-powermanagement
Requires:       lxqt-powermanagement
%description -n lxqt-powermanagement-l10n
This package provides translations for the lxqt-powermanagement package.

%package -n lxqt-runner-l10n
Summary:        Translations for lxqt-runner
Requires:       lxqt-runner
%description -n lxqt-runner-l10n
This package provides translations for the lxqt-runner package.

%package -n lxqt-session-l10n
Summary:        Translations for lxqt-session
Requires:       lxqt-session
%description -n lxqt-session-l10n
This package provides translations for the lxqt-session package.

%package -n lxqt-sudo-l10n
Summary:        Translations for lxqt-sudo
Requires:       lxqt-sudo
%description -n lxqt-sudo-l10n
This package provides translations for the lxqt-sudo package.

%package -n obconf-qt-l10n
Summary:        Translations for obconf-qt
Requires:       obconf-qt
%description -n obconf-qt-l10n
This package provides translations for the obconf-qt package.

%package -n pavucontrol-qt-l10n
Summary:        Translations for pavucontrol-qt
Requires:       pavucontrol-qt
%description -n pavucontrol-qt-l10n
This package provides translations for the pavucontrol-qt package.

%package -n pcmanfm-qt-l10n
Summary:        Translations for pcmanfm-qt
Requires:       pcmanfm-qt
%description -n pcmanfm-qt-l10n
This package provides translations for the pcmanfm-qt package.

%package -n qterminal-l10n
Summary:	Translations for QTerminal
Requires:       qterminal
%description -n qterminal-l10n
This package provides translations for the qterminal package.

%package -n qtermwidget-l10n
Summary:	Translations for qtermwdget
Requires:       qtermwidget
%description -n qtermwidget-l10n
This package provides translations for the qtermwidget package.

%prep
%autosetup


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
   %{cmake_lxqt} -DWITH_COMPTON_CONF=OFF \
%if 0%{?rhel}
                 -DWITH_LXQT_ADMIN=OFF \
%endif
                 ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang libfm-qt --with-qt
%find_lang liblxqt --with-qt
%find_lang lximage-qt --with-qt
%find_lang lxqt-about --with-qt
%if 0%{?fedora}
%find_lang lxqt-admin-user --with-qt
%find_lang lxqt-admin-time --with-qt
%endif
# package lxqt-config
%find_lang lxqt-config --with-qt
%find_lang lxqt-config-appearance --with-qt
%find_lang lxqt-config-brightness --with-qt
%find_lang lxqt-config-cursor --with-qt
%find_lang lxqt-config-file-associations --with-qt
%find_lang lxqt-config-input --with-qt
%find_lang lxqt-config-locale --with-qt
%find_lang lxqt-config-monitor --with-qt
# end package lxqt-config
%find_lang lxqt-config-globalkeyshortcuts --with-qt
%find_lang lxqt-config-notificationd --with-qt
%find_lang lxqt-notificationd --with-qt
%find_lang lxqt-openssh-askpass --with-qt
# package lxqt-panel
%find_lang lxqt-panel --with-qt
%find_lang clock --with-qt
%find_lang colorpicker --with-qt
%find_lang cpuload --with-qt
%find_lang desktopswitch --with-qt
%find_lang directorymenu --with-qt
%find_lang dom --with-qt
%find_lang kbindicator --with-qt
%find_lang mainmenu --with-qt
%find_lang mount --with-qt
%find_lang networkmonitor --with-qt
%find_lang quicklaunch --with-qt
%find_lang sensors --with-qt
%find_lang showdesktop --with-qt
%find_lang spacer --with-qt
%find_lang statusnotifier --with-qt
%find_lang sysstat --with-qt
%find_lang taskbar --with-qt
%find_lang tray --with-qt
%find_lang volume --with-qt
%find_lang worldclock --with-qt
# end package lxqt-panel
%find_lang lxqt-policykit-agent --with-qt
%find_lang lxqt-config-powermanagement --with-qt
%find_lang lxqt-powermanagement --with-qt
%find_lang lxqt-runner --with-qt
# package lxqt-session
%find_lang lxqt-config-session --with-qt
%find_lang lxqt-leave --with-qt
%find_lang lxqt-session --with-qt
# end package lxqt-session
%find_lang lxqt-sudo --with-qt
%find_lang obconf-qt --with-qt
%find_lang pavucontrol-qt --with-qt
%find_lang pcmanfm-qt --with-qt
%find_lang qterminal --with-qt
%find_lang qtermwidget --with-qt


# Main package has empty files section
%files

%files -n libfm-qt-l10n -f libfm-qt.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/libfm-qt/translations

%files -n liblxqt-l10n -f liblxqt.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/liblxqt

%files -n lximage-qt-l10n -f lximage-qt.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lximage-qt/translations

%files -n lxqt-about-l10n -f lxqt-about.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-about

%if 0%{?fedora}
%files -n lxqt-admin-l10n -f lxqt-admin-user.lang -f lxqt-admin-time.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-admin-user
%dir %{_datadir}/lxqt/translations/lxqt-admin-time
%endif

%files -n lxqt-config-l10n -f lxqt-config.lang -f lxqt-config-appearance.lang -f lxqt-config-brightness.lang -f lxqt-config-cursor.lang -f lxqt-config-file-associations.lang -f lxqt-config-input.lang -f lxqt-config-locale.lang -f lxqt-config-monitor.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-config
%dir %{_datadir}/lxqt/translations/lxqt-config-appearance
%dir %{_datadir}/lxqt/translations/lxqt-config-brightness
%dir %{_datadir}/lxqt/translations/lxqt-config-cursor
%dir %{_datadir}/lxqt/translations/lxqt-config-file-associations
%dir %{_datadir}/lxqt/translations/lxqt-config-input
%dir %{_datadir}/lxqt/translations/lxqt-config-locale
%dir %{_datadir}/lxqt/translations/lxqt-config-monitor

%files -n lxqt-globalkeys-l10n -f lxqt-config-globalkeyshortcuts.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-config-globalkeyshortcuts

%files -n lxqt-notificationd-l10n -f lxqt-config-notificationd.lang -f lxqt-notificationd.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-config-notificationd
%dir %{_datadir}/lxqt/translations/lxqt-notificationd

%files -n lxqt-openssh-askpass-l10n -f lxqt-openssh-askpass.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-openssh-askpass

%files -n lxqt-panel-l10n -f lxqt-panel.lang -f clock.lang -f colorpicker.lang -f cpuload.lang -f desktopswitch.lang -f directorymenu.lang -f dom.lang -f kbindicator.lang -f mainmenu.lang -f mount.lang -f networkmonitor.lang -f quicklaunch.lang -f sensors.lang -f showdesktop.lang -f spacer.lang -f statusnotifier.lang -f sysstat.lang -f taskbar.lang -f tray.lang -f volume.lang -f worldclock.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-panel

%files -n lxqt-policykit-l10n -f lxqt-policykit-agent.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-policykit-agent

%files -n lxqt-powermanagement-l10n -f lxqt-config-powermanagement.lang -f lxqt-powermanagement.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-config-powermanagement
%dir %{_datadir}/lxqt/translations/lxqt-powermanagement


%files -n lxqt-runner-l10n -f lxqt-runner.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-runner

%files -n lxqt-session-l10n -f lxqt-config-session.lang -f lxqt-leave.lang -f lxqt-session.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-config-session
%dir %{_datadir}/lxqt/translations/lxqt-leave
%dir %{_datadir}/lxqt/translations/lxqt-session


%files -n lxqt-sudo-l10n -f lxqt-sudo.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-sudo

%files -n obconf-qt-l10n -f obconf-qt.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/obconf-qt/translations

%files -n pavucontrol-qt-l10n -f pavucontrol-qt.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/pavucontrol-qt/translations

%files -n pcmanfm-qt-l10n -f pcmanfm-qt.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/pcmanfm-qt/translations

%files -n qterminal-l10n -f qterminal.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/qterminal/translations

%files -n qtermwidget-l10n -f qtermwidget.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/qtermwidget/translations


%changelog
* Sat Aug 04 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-1
- Update to version 0.13.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.2-6
- lxqt-l10n should require qterminal-l10n

* Wed Apr 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.2-5
- added qterminal-l10n subpackage

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.2-3
- no lxqt-admin on epel

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.2-2
- rebuilt

* Sun Jan 15 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.2-1
- initial package
