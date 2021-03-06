%global icondir %{_datadir}/icons/hicolor
%global commit ab838667d53c71c6cf8ac94dd109fcd009460530
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global reponame danmaQ
Name:		danmaq
Version:	0.2
Release:	1%{?dist}
Summary:	A small client side Qt program to play danmaku on any screen

License:	GPLv3
URL:		https://github.com/tuna/danmaQ
Source0:	%{url}/archive/%{shortcommit}/%{reponame}-%{shortcommit}.tar.gz

BuildRequires:	qt5-qtx11extras-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils

%description
DanmaQ is a small client side Qt program to play danmaku on any screen.

%prep
%setup -q -n %{reponame}-%{commit}

%build
mkdir build && cd build
%cmake ..
%make_build

%install
# install 
install -Dm 0755 build/src/%{reponame} %{buildroot}%{_bindir}/%{reponame}

# icon files
install -Dm0644 src/icons/statusicon.ico    %{buildroot}%{_datadir}/pixmaps/statusicon.ico
install -Dm0644 src/icons/statusicon.png    %{buildroot}%{_datadir}/pixmaps/statusicon.png
install -Dm0644 src/icons/statusicon_disabled.png    %{buildroot}%{_datadir}/pixmaps/statusicon_disabled.png
install -Dm0644 src/icons/statusicon.svg %{buildroot}%{icondir}/scalable/apps/statusicon.svg


# desktop file
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{reponame}.desktop <<EOF
[Desktop Entry]
Type=Application
Name=%{reponame}
Exec=%{reponame}
Icon=%{reponame}
Categories=Network
EOF

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{reponame}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:

%postun
if [ $1 -eq 0 ]; then
  /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null ||:
fi
/usr/bin/update-desktop-database &>/dev/null ||:

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null ||:

%files
%doc README.md
%license LICENSE
%{_bindir}/%{reponame}
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{reponame}.desktop

%changelog
* Sat Jul 29 2017 Zamir SUN <zsun@fedoraproject.org> - 0.2-1
- Change version to newest upstream tag

* Sat Jul 15 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.1.20170715git
- Initial with danmaQ git ab838667d53c71c6cf8ac94dd109fcd009460530
