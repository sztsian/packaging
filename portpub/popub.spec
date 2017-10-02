%global reponame popub
%global commit 4698f9acecb91b4ac6a195c1852c8582c9afadec
%global commitdate 20170920
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%if 0%{!?_unitdir:1}
%global _unitdir /usr/lib/systemd/system
%endif

Name:    %{reponame}
Version: 0
Release: 0.2.%{commitdate}git%{shortcommit}%{?dist}
Summary: Publish a service from localhost onto your server
License: GPLv3+
URL:     https://github.com/m13253/popub
Source0: %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

ExclusiveArch: %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires: systemd

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

%if ! 0%{?gotest:1}
%define gotest() go test -ldflags "${LDFLAGS:-}" %{?**}
%endif

%description
%{summary}.

%package local
Summary: Publish a service from localhost onto your server - client side
Obsoletes: portpub-local <= 0-0.2

%description local
%{summary}.
Local side package.

%package relay
Summary: Publish a service from localhost onto your server - server side
Obsoletes: portpub-relay <= 0-0.2

%description relay
%{summary}.
Server side package.

%prep
%setup -q -n %{name}-%{commit}

%build
cd %{reponame}-local
%gobuild -o %{reponame}-local

cd ../%{reponame}-relay
%gobuild -o %{reponame}-relay

%install
sed -i '/daemon-reload/d' systemd/Makefile
%make_install PREFIX=%{_prefix}

%files local
%doc README.md
%license COPYING
%{_bindir}/%{name}-local
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/local.d
%{_unitdir}/%{name}-local@.service
%{_userunitdir}/%{name}-local@.service

%files relay
%doc README.md
%license COPYING
%{_bindir}/%{name}-relay
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/relay.d
%{_unitdir}/%{name}-relay@.service
%{_userunitdir}/%{name}-relay@.service

%changelog
* Mon Oct 02 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.2.20170920git4698f9a
- Add support for EPEL

* Mon Sep 18 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.20170406git25cf44e
- Rename to popub
- Improve makefile

* Sat Sep 09 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.1.20170406gitccd226a
- Initial with git version ccd226a.
