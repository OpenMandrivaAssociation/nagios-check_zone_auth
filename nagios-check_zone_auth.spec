%define name	nagios-check_zone_auth
%define version	1.12
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Check DNS zones synchronisation
Group:		Networking/Other
License:	BSD
URL:		http://dns.measurement-factory.com/tools/nagios-plugins/check_zone_auth.html
Source0:	http://dns.measurement-factory.com/tools/nagios-plugins/src/check_zone_auth
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Use this plugin with Nagios to make sure that the authoritative nameservers for
a given zone remain in sync.

%prep

%build


%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
install -m 755 %{SOURCE0} %{buildroot}%{_datadir}/nagios/plugins

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_zone_auth.cfg <<'EOF'
define command{
	command_name	check_zone_auth
	command_line	%{_datadir}/nagios/plugins/check_zone_auth -Z $HOSTADDRESS$
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/nagios/plugins/check_zone_auth
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_zone_auth.cfg


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.12-2mdv2011.0
+ Revision: 612986
- the mass rebuild of 2010.1 packages

* Fri Nov 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2010.1
+ Revision: 465685
- new version

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.11-2mdv2010.0
+ Revision: 440232
- rebuild

* Sun Jan 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdv2009.1
+ Revision: 330895
- new version

* Mon Dec 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.9-3mdv2009.1
+ Revision: 314636
- now a noarch package

* Wed Aug 13 2008 Michael Scherer <misc@mandriva.org> 1.9-2mdv2009.0
+ Revision: 271401
- fix configuration

* Mon Jul 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.9-1mdv2009.0
+ Revision: 232349
- new version

* Fri Feb 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-4mdv2008.1
+ Revision: 168929
- fix configuration (thanks oden)

* Fri Feb 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-3mdv2008.1
+ Revision: 168914
- add a configuration file

* Fri Feb 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-2mdv2008.1
+ Revision: 168795
- not a noarch package, as nagios plugins installation directory is arch-dependant

* Fri Feb 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2008.1
+ Revision: 161107
- import nagios-check_zone_auth


* Fri Feb 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2008.1
- first release as independant package
