Summary:	Common C++ class framework for RTP/RTCP
Summary(pl.UTF-8):	Szkielet klas C++ dla RTP/RTCP
Name:		ccrtp
Version:	1.6.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/pub/gnu/ccrtp/%{name}-%{version}.tar.gz
# Source0-md5:	e6abc10abc0784f2aa4dd5597c1f1ad5
Patch0:		%{name}-gcc4.patch
Patch1:		%{name}-lt.patch
URL:		http://www.gnu.org/software/ccrtp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	commoncpp2-devel >= 1.5.0
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ccRTP is a generic, extensible and efficient C++ framework for
developing applications based on the Real-Time Transport Protocol
(RTP) from the IETF. It is based on Common C++ and provides a full
RTP/RTCP stack for sending and receiving of realtime data by the use
of send and receive packet queues. ccRTP supports unicast,
multi-unicast and multicast, manages multiple sources, handles RTCP
automatically, supports different threading models and is generic as
for underlying network and transport protocols.

%description -l pl.UTF-8
ccRTP jest ogólnym, rozszerzalnym i efektywnym szkieletem C++ do
rozwijania aplikacji bazujących na transporcie czasu rzeczywistego
(RTP) z IETF. Bazuje na Common C++ i udostępnia pełen stos RTP/RTCP do
wysyłania i odbierania danych w czasie rzeczywistym z użyciem kolejek
wysyłania i odbierania pakietów. ccRTP obsługuje unicasty,
multi-unicasty i multicasty, zarządza wieloma źródłami, obsługuje
automatycznie RTCP, wspiera różne modele wątkowania i jest ogólny dla
podstawowych sieci i protokołów transportowych.

%package devel
Summary:	Header files for ccrtp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ccrtp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	commoncpp2-devel

%description devel
Header files for ccrtp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ccrtp.

%package static
Summary:	Static ccrtp library
Summary(pl.UTF-8):	Statyczna biblioteka ccrtp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ccrtp library.

%description static -l pl.UTF-8
Statyczna biblioteka ccrtp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING.addendum README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*.html doc/html/*.*g*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/ccrtp
%{_pkgconfigdir}/*.pc
%{_infodir}/*.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
