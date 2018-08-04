Name:		qterminal
Version:	0.9.0
Release:	1%{?dist}
License:	GPLv2
URL:		https://github.com/qterminal/qterminal
Source0:	https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Summary:	Advanced Qt5-based terminal emulator


BuildRequires:	desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(lxqt) >= 0.13.0
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(qtermwidget5) = %{version}
BuildRequires:  qt5-qttools-devel

# Require qtermwidget to be the same version, as suggested by upstream
Requires:       qtermwidget = %{version}

Provides:       %{name}-common = %{version}-%{release}
Provides:       %{name}-qt5 = %{version}-%{release}
Obsoletes:      %{name}-common < %{version}-%{release}
Obsoletes:      %{name}-qt5 < %{version}-%{release}

%description
Advanced Qt5-based terminal emulator with many useful bells and whistles.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_lxqt} -DPULL_TRANSLATIONS=NO ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}_drop.desktop


%post
/bin/touch --no-create %{_kf5_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%license LICENSE
%doc AUTHORS CHANGELOG CONTRIBUTING.md README.md
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}_drop.desktop
%{_datadir}/icons/*/*


%changelog
* Sat Aug 04 2018 Zamir SUN <zsun@fedoraproject.org> - 0.9.0-1
- Update to version 0.9.0
bump

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 22 2017 Christian Dersch <lupinix@mailbox.org> - 0.7.1-2
- require qtermwidget to be the same version as qterminal

* Wed Apr 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.7.1-1
- new version
- removed Qt4 build (no longer supported by upstream)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 2 2015 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-4
- Qt5 version added

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-2
- Rebuild with new qtermwidget

* Tue Nov 04 2014 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-1
- Version bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-5
- Next git snapshot
- Changelog dates (year) fixed

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-3
- Source URL update
- second desktop validate added

* Mon May 06 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-2
- Source URL update

* Mon May 06 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-1
- initial packaging for Fedora
