%global _icondir %{_datadir}/icons/hicolor

Name:           xfce4-statusnotifier-plugin
Version:        0.1.0
Release:        1%{?dist}
Summary:        Panel area status notifier plugin for Xfce4
License:        LGPLv3
URL:            http://www.xfce.org/
Source0:        https://git.xfce.org/panel-plugins/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRequires:  xfce4-dev-tools
BuildRequires:  libtool
BuildRequires:  gtk3-devel
BuildRequires:  libxfce4util-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  xfce4-panel-devel
BuildRequires:  libdbusmenu-gtk3-devel
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils

%description
This plugin provides a panel area for status notifier items (application
indicators). Applications may use these items to display their status and
interact with user. This technology is a modern alternative to systray and
has the freedesktop.org specification.

%prep
%setup -q

%build
./autogen.sh --prefix=%{_prefix}
%make_build

%install
%make_install
if [ ! -d %{buildroot}/%{_libdir} ]; then
mv %{buildroot}/usr/lib %{buildroot}/%{_libdir}
fi
#install -Dm 0755 %{buildroot}/usr/lib/xfce4/panel/plugins/libstatusnotifier.la %{buildroot}%{_libdir}/libstatusnotifier.la
#install -Dm 0755 %{buildroot}/usr/lib/xfce4/panel/plugins/libstatusnotifier.so %{buildroot}%{_libdir}/libstatusnotifier.so
#rm %{buildroot}/usr/lib/xfce4/panel/plugins/libstatusnotifier.* -f

%post
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%{_libdir}/xfce4/panel/plugins/libstatusnotifier.*
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/icons/hicolor/*/apps/xfce4-statusnotifier-plugin.png
%{_datadir}/icons/hicolor/*/apps/xfce4-statusnotifier-plugin.svg
%{_datadir}/xfce4/panel/plugins/statusnotifier.desktop

%changelog
* Tue Jul 25 2017 Zamir SUN <zsun@fedoraproject.org> - 0.1.0-1
- Initial xfce4-statusnotifier-plugin

