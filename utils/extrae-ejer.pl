#!/usr/bin/env perl

use strict;
use warnings;
use v5.14;

use File::Slurper qw(read_text);

my @mds = glob "../txt/*.md";
for my $file (@mds) {

  my $contenido = read_text $file;
  my @ejemplos = ( $contenido =~ /```(.+?)```/sg );

  say join("\n",map("<section><pre><code>$_</code></pre></section>\n",@ejemplos));
  
}
  
