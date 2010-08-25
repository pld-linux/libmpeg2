Summary:	MPEG-2 Decoder
Summary(pl.UTF-8):	Dekoder plików MPEG-2
Name:		libmpeg2
Version:	0.5.1
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://libmpeg2.sourceforge.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	0f92c7454e58379b4a5a378485bbd8ef
Patch0:		%{name}-ppc.patch
URL:		http://libmpeg2.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
%ifarch ppc
# version with altivec support (almost?) fixed
BuildRequires:	gcc >= 5:3.3.2-3
%endif
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}
Obsoletes:	mpeg2dec < 0.5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MPEG-2 Decoder.

%description -l pl.UTF-8
Dekoder MPEG-2.

%package libs
Summary:	MPEG-2 Decoder library
Summary(pl.UTF-8):	Biblioteka dekodująca pliki MPEG-2
Group:		Libraries
Obsoletes:	mpeg2dec-lib < 0.5.1

%description libs
MPEG-2 Decoder library and extract_mpeg2 utility.

%description libs -l pl.UTF-8
Biblioteka dekodująca pliki MPEG-2 i narzędzie extract_mpeg2.

%package devel
Summary:	MPEG-2 Decoder development files
Summary(pl.UTF-8):	Pliki dla programistów używających dekodera MPEG-2
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}
Obsoletes:	mpeg2dec-devel < 0.5.1

%description devel
MPEG-2 Decoder development files.

%description devel -l pl.UTF-8
Pliki dla programistów używających dekodera MPEG-2.

%package static
Summary:	MPEG-2 Decoder static libraries
Summary(pl.UTF-8):	Statyczne biblioteki dekodera MPEG-2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	mpeg2dec-static < 0.5.1

%description static
MPEG-2 Decoder static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki dekodera MPEG-2.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags} -DCOFFEE_BREAK=1"
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?debug:--enable-debug} \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpeg2dec
%{_mandir}/man1/mpeg2dec.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/corrupt_mpeg2
%attr(755,root,root) %{_bindir}/extract_mpeg2
%attr(755,root,root) %{_libdir}/libmpeg2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpeg2.so.0
%attr(755,root,root) %{_libdir}/libmpeg2convert.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpeg2convert.so.0
%{_mandir}/man1/extract_mpeg2.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpeg2.so
%attr(755,root,root) %{_libdir}/libmpeg2convert.so
%{_libdir}/libmpeg2.la
%{_libdir}/libmpeg2convert.la
%{_includedir}/mpeg2dec
%{_pkgconfigdir}/libmpeg2.pc
%{_pkgconfigdir}/libmpeg2convert.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmpeg2.a
%{_libdir}/libmpeg2convert.a
