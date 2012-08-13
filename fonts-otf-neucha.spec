Name:		fonts-otf-neucha
Summary:	Neucha font by Jovanny Lemonad
Version:	0.1
Release:	0.1
License:	OFL
Group:		System/Fonts/True type
URL:		http://jovanny.ru/free-fonts.html
Source0:	neucha.otf.xz
BuildArch:	noarch
BuildRequires:	freetype-tools

%description
You will throw tomatoes at me when I say that the font Neucha was invented
for the sake of one and only one phrase: “I love you”. It was 2005 and I was
in love. The first version of the font was done in 8 hours. I recently redid
this fastfont from scratch, some glyphs have changed greatly but most of them
I did not touch – just polished. Neucha very strong in terms of energy and I
love it. Neucha translated from the Russian language means “not knowing how
to create fonts right”.

%prep
%setup -qcT
unxz -c %{SOURCE0} > neucha.otf

%build

%install
%__mkdir_p %{buildroot}%{_xfontdir}/OTF/neucha

%__install -m 644 *.otf %{buildroot}%{_xfontdir}/OTF/neucha
ttmkfdir %{buildroot}%{_xfontdir}/OTF/neucha -o %{buildroot}%{_xfontdir}/OTF/neucha/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/OTF/neucha/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/OTF/neucha \
    %{buildroot}%_sysconfdir/X11/fontpath.d/otf-neucha:pri=50

%files
%defattr(0644,root,root,0755)
%dir %{_xfontdir}/OTF/neucha
%{_xfontdir}/OTF/neucha/*.otf
%verify(not mtime) %{_datadir}/fonts/OTF/neucha/fonts.dir
%{_xfontdir}/OTF/neucha/fonts.scale
%{_sysconfdir}/X11/fontpath.d/otf-neucha:pri=50
