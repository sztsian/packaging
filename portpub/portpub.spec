%global reponame portpub
%global commit ccd226a3fc7e59d89c77391be3c556e34d7c23a8
%global commitdate 20170406
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%if 0%{!?_unitdir:1}
%global _unitdir /usr/lib/systemd/system
%endif

Name:    %{reponame}
Version: 0
Release: 0.1.%{commitdate}git%{shortcommit}%{?dist}
Summary: Publish a service from localhost onto your server

License: GPLv3+
URL:     https://github.com/m13253/%{reponame}
Source0: %{url}/archive/%{commit}/%{reponame}-%{shortcommit}.tar.gz
Source1: portpub-conf
BuildRequires: golang-bin
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}

%description
%{summary}.

%package local
Summary: Publish a service from localhost onto your server - client side
Requires: systemd-units

%package relay
Summary: Publish a service from localhost onto your server - server side
Requires: systemd-units

%description -n %{reponame}-local
%{summary}.
Local side package.

%description -n %{reponame}-relay
%{summary}.
Server side package.

%prep
%setup -q -n %{reponame}-%{commit}

%build
sed -i '/#ExecStart=\/usr\/local/c ExecStart=\/usr\/bin\/portpub-local ${LOCAL}:${LOCALPORT} ${SERVER}:${SERVERPORT} ${PASSWORD}' *.service
sed -i 's/and uncomment the following line/in \/etc\/sysconfig\/portpub-local and uncomment/' *.service
sed -i '/# Fill in/i EnvironmentFile=-\/etc\/portpub-local' *.service
sed -i 's/portpub-local/portpub-relay/g' %{reponame}-relay.service
cd %{reponame}-local
%gobuild -o %{reponame}-local

cd ../%{reponame}-relay
%gobuild -o %{reponame}-relay

%install
install -dm 755 %{buildroot}%{_unitdir}
install -dm 755 %{buildroot}%{_bindir}
install -dm 755 %{buildroot}%{_sysconfdir}
install -m 0755 %{reponame}-local/%{reponame}-local %{buildroot}%{_bindir}/
install -m 0755 %{reponame}-relay/%{reponame}-relay %{buildroot}%{_bindir}/
install -m 0644 %{reponame}-*.service %{buildroot}%{_unitdir}/
install -m 0644 %{_sourcedir}/portpub-conf %{buildroot}%{_sysconfdir}/%{reponame}-local
install -m 0644 %{_sourcedir}/portpub-conf %{buildroot}%{_sysconfdir}/%{reponame}-relay


%files -n %{reponame}-local
%doc README.md
%license COPYING
%{_bindir}/%{reponame}-local
%config(noreplace) %{_sysconfdir}/%{reponame}-local
%{_unitdir}/%{reponame}-local.service

%files -n %{reponame}-relay
%doc README.md
%license COPYING
%{_bindir}/%{reponame}-relay
%config(noreplace) %{_sysconfdir}/%{reponame}-relay
%{_unitdir}/%{reponame}-relay.service

%changelog
* Sat Sep 09 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.1.20170406gitccd226a
- Initial with git version ccd226a.
