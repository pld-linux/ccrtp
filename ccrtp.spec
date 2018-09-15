#
# Conditional build:
%bcond_with	gcrypt	# use libgcrypt instead of OpenSSL (ucommon in PLD uses OpenSSL by default)

Summary:	Common C++ class framework for RTP packets
Summary(pl.UTF-8):	Szkielet klas C++ dla pakietów RTP
Name:		ccrtp
Version:	2.1.2
Release:	4
License:	GPL v2+ with runtime exception
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/ccrtp/%{name}-%{version}.tar.gz
# Source0-md5:	e6792cbd8b705901c205a509bd7f812f
Patch0:		%{name}-info.patch
Patch1:		%{name}-openssl.patch
Patch2:		%{name}-am.patch
URL:		http://www.gnu.org/software/ccrtp/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	doxygen >= 1.8.0
%{?with_gcrypt:BuildRequires:	libgcrypt-devel >= 1.2.3}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
%{!?with_gcrypt:BuildRequires:	openssl-devel}
BuildRequires:	pkgconfig
BuildRequires:	ucommon-devel >= 6.2.2
Requires:	ucommon >= 6.2.2
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
%{?with_gcrypt:Requires:	libgcrypt-devel >= 1.2.3}
Requires:	libstdc++-devel
%{!?with_gcrypt:Requires:	openssl-devel}
Requires:	ucommon-devel >= 6.2.2

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
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
# LIBGCRYPT_CONFIG is a hack to disable libgcrypt and pass to openssl detection
%configure \
	%{!?with_gcrypt:LIBGCRYPT_CONFIG=/nonexisting}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.addendum ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libccrtp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libccrtp.so.3

%files devel
%defattr(644,root,root,755)
%doc doc/html/*.{css,html,js,png}
%attr(755,root,root) %{_libdir}/libccrtp.so
%{_libdir}/libccrtp.la
%{_includedir}/ccrtp
%{_pkgconfigdir}/libccrtp.pc
%{_infodir}/ccrtp.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libccrtp.a
