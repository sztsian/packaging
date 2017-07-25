Name:           xfce4-statusnotifier-plugin
Version:        0.1.0
Release:        1%{?dist}
Summary:        Panel area status notifier plugin for Xfce4
License:        LGPLv3
URL:            http://www.xfce.org/
Source0:        https://git.xfce.org/panel-plugins/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRequires:  xfce4-dev-tools libtool gtk3-devel libxfce4util-devel libxfce4ui-devel xfce4-panel-devel libdbusmenu-gtk3-devel
BuildRequires:  gcc-c++

%description
Panel area status notifier plugin for Xfce4.

%prep
%setup -q

%build
./autogen.sh --prefix=/usr
#./autogen.sh --libdir=$RPM_BUILD_ROOT%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
find %{buildroot} -iname "*.so" -exec mv {} %{buildroot}%{_libdir}/ \;
#find %{buildroot} -iname "*.la" -exec rm -f {} \;

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

#%files
#%{_libdir}/*.so*
#%license COPYING
#%dir %{_qt5_qmldir}/GSettings.1.0/
#%{_qt5_qmldir}/GSettings.1.0/libGSettingsQmlPlugin.so
#%{_qt5_qmldir}/GSettings.1.0/plugins.qmltypes
#%{_qt5_qmldir}/GSettings.1.0/qmldir

#%files devel
#%license COPYING
#%dir %{_qt5_headerdir}/QGSettings/
#%{_qt5_headerdir}/QGSettings/*
#%{_libdir}/pkgconfig/%{name}.pc
#%{_libdir}/lib%{name}.so

%changelog
* Tue Jul 25 2017 Zamir SUN <zsun@fedoraproject.org> - 0.1.0-1
- Initial xfce4-statusnotifier-plugin

