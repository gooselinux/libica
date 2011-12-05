Summary: Library for accessing ICA hardware crypto on IBM zSeries
Name: libica
Version: 2.0.3
Release: 2%{?dist}
License: CPL
Group: System Environment/Libraries
URL: http://sourceforge.net/projects/opencryptoki/
Source0: http://downloads.sourceforge.net/opencryptoki/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: openssl-devel
BuildRequires: autoconf automake libtool
ExclusiveArch: s390 s390x
Provides: %{name}-utils = 2.0.2-2
Obsoletes: %{name}-utils < 2.0.2-2

%description
A library of functions and utilities for accessing ICA hardware crypto on
IBM zSeries.


%package devel
Summary: Development tools for programs to access ICA hardware crypto on IBM zSeries
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: openssl-devel

%description devel
The libica-devel package contains the header files and static
libraries necessary for developing programs accessing ICA hardware crypto on
IBM zSeries.


%prep
%setup -q -n %{name}-2

# fix EOLs
sed -i -e 's/\r//g' LICENSE

sh ./bootstrap.sh


%build
%configure --disable-static
# paralell make doesn't work
make AM_CFLAGS="-fno-strict-aliasing"


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libica.la


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE
%{_bindir}/icainfo
%{_bindir}/icastats
%{_libdir}/libica-2.0.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/libica.so


%changelog
* Fri May 21 2010 Dan Horák <dan[at]danny.cz> - 2.0.3-2
- rebuilt with -fno-strict-aliasing (#593779)
- Resolves: #593779

* Thu Apr 22 2010 Dan Horák <dan[at]danny.cz> - 2.0.3-1
- updated to 2.0.3 (#582607)
- Resolves: #582607

* Mon Apr 12 2010 Dan Horák <dan[at]danny.cz> - 2.0.2-3
- add SIGILL handler for add_entropy (#581520)
- Resolves: #581520

* Tue Feb 16 2010 Dan Horák <dan[at]danny.cz> - 2.0.2-2
- dropped the utils sub-package
- Related: #543948

* Tue Dec 08 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.0.2-1.1
- Rebuilt for RHEL 6

* Mon Aug 17 2009 Dan Horák <dan[at]danny.cz> - 2.0.2-1
- update to 2.0.2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr  1 2009 Dan Horák <dan[at]danny.cz> - 2.0.1-1
- update to 2.0.1

* Mon Mar 23 2009 Dan Horák <dan[at]danny.cz> - 2.0-1
- update to 2.0
- spec file cleanup before submitting to Fedora

* Sun Sep 14 2008 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-8.el5
- Added the icainfo tool to libica (#439484)

* Tue Apr 01 2008 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-7.el5
- Fixed build of libica with latest AES & SHA feature (#439390)

* Tue Jan 15 2008 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-6.el5
- Added Software Support for CP Assist Instructions AES & SHA (#318971)

* Thu Nov 23 2006 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-5.el5
- Fixed requires bug where devel packages would get wrong arch lib (#215908)

* Fri Oct 13 2006 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-4
- Fixed bug where libica fails to initialize when no crypto hardware is
  available (#210504)
- Only build libica for s390(x), really only needed there.

* Fri Sep 08 2006 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-3
- Build for other archs as well due to openCryptoki requirement (#184631)

* Fri Jul 14 2006 Tim Powers <timp@redhat.com> - 1.3.7-2
- rebuild

* Tue Jun 13 2006 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-1
- Update to libica-1.3.7 final
- Fixed build on latest devel tree

* Tue Apr 04 2006 Phil Knirsch <pknirsch@redhat.com> - 1.3.6-rc3-1
- Initial package.
