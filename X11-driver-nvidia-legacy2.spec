#
# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
%bcond_without	up		# without up packages
%bcond_without	smp		# without smp packages
%bcond_without	kernel		# without kernel packages
%bcond_without	userspace	# don't build userspace programs
%bcond_with	verbose		# verbose build (V=1)
%bcond_with	grsec_kernel	# build for kernel-grsecurity

%if %{without kernel}
%undefine	with_dist_kernel
%endif
%if %{with kernel} && %{with dist_kernel} && %{with grsec_kernel}
%define	alt_kernel	grsecurity
%endif
%if "%{_alt_kernel}" != "%{nil}"
%undefine	with_userspace
%endif

%define		_nv_ver		96.43.01
%define		_min_x11	6.7.0
%define		_rel	61
#

%define		pname	X11-driver-nvidia-legacy2
Summary:	Linux Drivers for NVIDIA GeForce/Quadro Chips
Summary(pl):	Sterowniki do kart graficznych NVIDIA GeForce/Quadro
Name:		%{pname}%{_alt_kernel}
Version:	%{_nv_ver}
Release:	%{_rel}
License:	nVidia Binary
Group:		X11
Source0:	http://download.nvidia.com/XFree86/Linux-x86/%{_nv_ver}/NVIDIA-Linux-x86-%{_nv_ver}-pkg1.run
# Source0-md5:	66f8b5e243aad22162e40d0f05f0bf1e
Source1:	http://download.nvidia.com/XFree86/Linux-x86_64/%{_nv_ver}/NVIDIA-Linux-x86_64-%{_nv_ver}-pkg1.run
# Source1-md5:	1cb134675bbdce8e172a0edc78618ed3
Source2:	%{pname}-settings.desktop
Source3:	%{pname}-xinitrc.sh
Patch0:		%{pname}-GL.patch
URL:		http://www.nvidia.com/object/unix.html
%if %{with kernel}
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.7}
BuildRequires:	%{kgcc_package}
BuildRequires:	rpmbuild(macros) >= 1.330
%endif
BuildRequires:	sed >= 4.0
BuildConflicts:	XFree86-nvidia
Requires:	X11-Xserver
Requires:	X11-libs >= %{_min_x11}
Requires:	X11-modules >= %{_min_x11}
Provides:	X11-OpenGL-core
Provides:	X11-OpenGL-libGL
Provides:	XFree86-OpenGL-core
Provides:	XFree86-OpenGL-libGL
Obsoletes:	Mesa
Obsoletes:	Mesa-libGL
Obsoletes:	X11-OpenGL-core
Obsoletes:	X11-OpenGL-libGL
Obsoletes:	XFree86-OpenGL-core
Obsoletes:	XFree86-OpenGL-libGL
Obsoletes:	XFree86-driver-nvidia
Obsoletes:	XFree86-nvidia
Conflicts:	XFree86-OpenGL-devel <= 4.2.0-3
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLcore.so.1
%define		_prefix		/usr/X11R6
%ifarch %{x8664}
%define		_libdir32	%{_prefix}/lib
%endif

%description
This driver set adds improved 2D functionality to the Xorg X server as
well as high performance OpenGL acceleration, AGP support, support for
most flat panels, and 2D multiple monitor support. Supported hardware:
modern NVIDIA GeForce (from GeForce2 MX) and Quadro (Quadro4 and up)
based graphics accelerators.

The older graphics chips are unsupported:
- NV1 and RIVA 128/128ZX chips are supported in the base Xorg install
  (nv driver)
- TNT/TNT2/GeForce 256/GeForce2 Ultra/Quadro2 are suported by -legacy
  drivers.

%description -l pl
Usprawnione sterowniki dla kart graficznych NVIDIA do serwera Xorg,
daj±ce wysokowydajn± akceleracjê OpenGL, obs³ugê AGP i wielu monitorów
2D. Obs³uguj± w miarê nowe karty NVIDIA GeForce (od wersji GeForce2
MX) oraz Quadro (od wersji Quadro4) do serwera Xorg/XFree86.

Starsze uk³ady graficzne NVIDIA nie s± obs³ugiwane przez ten pakiet:
- NV1 i Riva 128/128ZX s± obs³ugiwane przez sterownik nv z Xorg.
- TNT/TNT2/GeForce 256/GeForce2 Ultra/Quadro2 obs³ugiwane s± przez
  sterownik NVIDIA w wersji -legacy.

%package devel
Summary:	OpenGL for X11R6 development (only gl?.h)
Summary(pl):	Pliki nag³ówkowe OpenGL dla systemu X11R6 (tylko gl?.h)
Group:		X11/Development/Libraries
Requires:	%{pname} = %{version}-%{release}
Provides:	OpenGL-devel-base
Obsoletes:	OpenGL-devel-base
Obsoletes:	XFree86-driver-nvidia-devel
Conflicts:	XFree86-OpenGL-devel < 4.3.99.902-0.3

%description devel
Base headers (only gl?.h) for OpenGL for X11R6 for nvidia drivers.

%description devel -l pl
Podstawowe pliki nag³ówkowe (tylko gl?.h) OpenGL dla systemu X11R6 dla
sterowników nvidii.

%package progs
Summary:	Tools for advanced control of nVidia graphic cards
Summary(pl):	Narzêdzia do zarz±dzania kartami graficznymi nVidia
Group:		Applications/System
Requires:	%{pname} = %{version}-%{release}
Obsoletes:	XFree86-driver-nvidia-progs

%description progs
Tools for advanced control of nVidia graphic cards.

%description progs -l pl
Narzêdzia do zarz±dzania kartami graficznymi nVidia.

%package -n kernel%{_alt_kernel}-video-nvidia-legacy2
Summary:	nVidia kernel module for nVidia Architecture support
Summary(de):	Das nVidia-Kern-Modul für die nVidia-Architektur-Unterstützung
Summary(pl):	Modu³ j±dra dla obs³ugi kart graficznych nVidia
Version:	%{_nv_ver}
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.7.7-10
%{?with_dist_kernel:%requires_releq_kernel_up}
Provides:	X11-driver-nvidia-legacy2(kernel)
Obsoletes:	XFree86-nvidia-kernel

%description -n kernel%{_alt_kernel}-video-nvidia-legacy2
nVidia Architecture support for Linux kernel.

%description -n kernel%{_alt_kernel}-video-nvidia-legacy2 -l de
Die nVidia-Architektur-Unterstützung für den Linux-Kern.

%description -n kernel%{_alt_kernel}-video-nvidia-legacy2 -l pl
Obs³uga architektury nVidia dla j±dra Linuksa. Pakiet wymagany przez
sterownik nVidii dla Xorg/XFree86.

%package -n kernel%{_alt_kernel}-smp-video-nvidia-legacy2
Summary:	nVidia kernel module for nVidia Architecture support
Summary(de):	Das nVidia-Kern-Modul für die nVidia-Architektur-Unterstützung
Summary(pl):	Modu³ j±dra dla obs³ugi kart graficznych nVidia
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.7.7-10
%{?with_dist_kernel:%requires_releq_kernel_smp}
Provides:	X11-driver-nvidia-legacy2(kernel)
Obsoletes:	XFree86-nvidia-kernel

%description -n kernel%{_alt_kernel}-smp-video-nvidia-legacy2
nVidia Architecture support for Linux kernel SMP.

%description -n kernel%{_alt_kernel}-smp-video-nvidia-legacy2 -l de
Die nVidia-Architektur-Unterstützung für den Linux-Kern SMP.

%description -n kernel%{_alt_kernel}-smp-video-nvidia-legacy2 -l pl
Obs³uga architektury nVidia dla j±dra Linuksa SMP. Pakiet wymagany
przez sterownik nVidii dla Xorg/XFree86.

%prep
cd %{_builddir}
rm -rf NVIDIA-Linux-x86*-%{_nv_ver}-pkg*
%ifarch %{ix86}
/bin/sh %{SOURCE0} --extract-only
%setup -qDT -n NVIDIA-Linux-x86-%{_nv_ver}-pkg1
%else
/bin/sh %{SOURCE1} --extract-only
%setup -qDT -n NVIDIA-Linux-x86_64-%{_nv_ver}-pkg1
%endif
%patch0 -p1
sed -i 's:-Wpointer-arith::' usr/src/nv/Makefile.kbuild

%build
%if %{with kernel}
cd usr/src/nv/
ln -sf Makefile.kbuild Makefile
cat >> Makefile <<'EOF'

$(obj)/nv-kernel.o: $(src)/nv-kernel.o.bin
	cp $< $@
EOF
mv nv-kernel.o{,.bin}
%build_kernel_modules -m nvidia
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with userspace}
install -d $RPM_BUILD_ROOT%{_libdir}/modules/{drivers,extensions} \
	$RPM_BUILD_ROOT{/usr/include/GL,/usr/%{_lib}/tls,%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},/etc/X11/xinit/xinitrc.d}

ln -sf $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_prefix}/../lib

install usr/bin/nvidia-settings $RPM_BUILD_ROOT%{_bindir}
install usr/bin/nvidia-xconfig $RPM_BUILD_ROOT%{_bindir}
install usr/share/pixmaps/nvidia-settings.png $RPM_BUILD_ROOT%{_pixmapsdir}
install usr/share/man/man1/nvidia-[sx]* $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/nvidia-settings.desktop
install %{SOURCE3} $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/nvidia-settings.sh
install usr/lib/libnvidia-tls.so.%{version} $RPM_BUILD_ROOT/usr/%{_lib}
install usr/lib/tls/libnvidia-tls.so.%{version} $RPM_BUILD_ROOT/usr/%{_lib}/tls
install usr/lib/libGL{,core}.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install usr/X11R6/lib/modules/extensions/libglx.so.%{version} \
	$RPM_BUILD_ROOT%{_libdir}/modules/extensions

install usr/X11R6/lib/modules/drivers/nvidia_drv.so $RPM_BUILD_ROOT%{_libdir}/modules/drivers
install usr/X11R6/lib/libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install usr/X11R6/lib/libXvMCNVIDIA.a $RPM_BUILD_ROOT%{_libdir}
install usr/include/GL/*.h	$RPM_BUILD_ROOT/usr/include/GL

ln -sf libGL.so.1 $RPM_BUILD_ROOT%{_libdir}/libGL.so
ln -sf libglx.so.%{version} $RPM_BUILD_ROOT%{_libdir}/modules/extensions/libglx.so
ln -sf libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libXvMCNVIDIA.so

# OpenGL ABI for Linux compatibility
ln -sf %{_libdir}/libGL.so.1 $RPM_BUILD_ROOT/usr/%{_lib}/libGL.so.1
ln -sf %{_libdir}/libGL.so $RPM_BUILD_ROOT/usr/%{_lib}/libGL.so
%endif

%if %{with kernel}
%install_kernel_modules -m usr/src/nv/nvidia -d misc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
cat << EOF

 *******************************************************
 *                                                     *
 *  NOTE:                                              *
 *  You must install:                                  *
 *  kernel(24)(-smp)-video-nvidia-legacy2-%{version}     *
 *  for this driver to work                            *
 *                                                     *
 *******************************************************

EOF

%postun	-p /sbin/ldconfig

%post	-n kernel%{_alt_kernel}-video-nvidia-legacy2
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-video-nvidia-legacy2
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-smp-video-nvidia-legacy2
%depmod %{_kernel_ver}smp

%postun	-n kernel%{_alt_kernel}-smp-video-nvidia-legacy2
%depmod %{_kernel_ver}smp

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc LICENSE
%doc usr/share/doc/{README.txt,NVIDIA_Changelog,XF86Config.sample}
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%attr(755,root,root) %{_libdir}/libGL.so
%attr(755,root,root) %{_libdir}/libGLcore.so.*.*
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so.*.*
%dir /usr/%{_lib}/tls
%attr(755,root,root) /usr/%{_lib}/libnvidia-tls.so.*.*.*
%attr(755,root,root) /usr/%{_lib}/tls/libnvidia-tls.so.*.*.*
%attr(755,root,root) /usr/%{_lib}/libGL.so.1
%attr(755,root,root) /usr/%{_lib}/libGL.so
%attr(755,root,root) %{_libdir}/modules/extensions/libglx.so*
%attr(755,root,root) %{_libdir}/modules/drivers/nvidia_drv.so
%endif

%if %{with kernel}
%if %{with up} || %{without dist_kernel}
%files -n kernel%{_alt_kernel}-video-nvidia-legacy2
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*.ko*
%endif

%if %{with smp} && %{with dist_kernel}
%files -n kernel%{_alt_kernel}-smp-video-nvidia-legacy2
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/*.ko*
%endif
%endif

%if %{with userspace}
%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so
/usr/include/GL/*.h
%{_libdir}/libXvMCNVIDIA.a

%files progs
%defattr(644,root,root,755)
%doc usr/share/doc/nvidia-settings-user-guide.txt
%attr(755,root,root) %{_bindir}/nvidia-settings
%attr(755,root,root) %{_bindir}/nvidia-xconfig
%attr(755,root,root) /etc/X11/xinit/xinitrc.d/*.sh
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_pixmapsdir}/*
%endif
