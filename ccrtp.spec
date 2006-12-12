Summary:	Common C++ class framework for RTP/RTCP
Summary(pl):	Szkielet klas C++ dla RTP/RTCP
Name:		ccrtp
Version:	1.5.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/pub/gnu/ccrtp/%{name}-%{version}.tar.gz
# Source0-md5:	019754d20b46b1b23f3bc368aa58d662
URL:		http://www.gnu.org/software/ccrtp/
BuildRequires:	commoncpp2-devel
BuildRequires:	doxygen
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

%description -l pl
ccRTP jest ogólnym, rozszerzalnym i efektywnym szkieletem C++ do
rozwijania aplikacji bazuj±cych na transporcie czasu rzeczywistego
(RTP) z IETF. Bazuje na Common C++ i udostêpnia pe³en stos RTP/RTCP do
wysy³ania i odbierania danych w czasie rzeczywistym z u¿yciem kolejek
wysy³ania i odbierania pakietów. ccRTP obs³uguje unicasty,
multi-unicasty i multicasty, zarz±dza wieloma ¼ród³ami, obs³uguje
automatycznie RTCP, wspiera ró¿ne modele w±tkowania i jest ogólny dla
podstawowych sieci i protoko³ów transportowych.

%package devel
Summary:	Header files for ccrtp library
Summary(pl):	Pliki nag³ówkowe biblioteki ccrtp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	commoncpp2-devel

%description devel
Header files for ccrtp library.

%description devel -l pl
Pliki nag³ówkowe biblioteki ccrtp.

%package static
Summary:	Static ccrtp library
Summary(pl):	Statyczna biblioteka ccrtp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ccrtp library.

%description static -l pl
Statyczna biblioteka ccrtp.

%prep
%setup -q

%build
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
