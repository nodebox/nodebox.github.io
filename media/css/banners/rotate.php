<?php

/**
 * randomly select an image from the current directory and return it
 *
 * @todo - consider accepting a local path as $_GET['img'] for overrides
 * to remain compatible with Marinelli's rotate.php
 * 
 * (but why? why possible use case is there for linking to 
 * rotate.php?img=file.gif instead of straight to file.gif?)
 */

$file_types = array( 
  'gif'  => 'image/gif',
  'jpg'  => 'image/jpeg',
  'jpeg' => 'image/jpeg',
  'png'  => 'image/png'
) ;

$regex = '/\.(' . implode('|',array_keys($file_types)) . ')$/i' ;
$files = array() ;

$directory = opendir(".");
while ( FALSE !== ($file = readdir( $directory )) ) {
  if ( preg_match( $regex, $file ) ) {
    $files[] = $file ;
  }
}

if ( !empty( $files ) ) {

  $which   = rand(0,sizeof($files)-1) ;

  if ( $file = file_get_contents( $files[$which] ) ) {

    $parts   = explode('.',$files[$which]) ;
    $ext     = strtolower($parts[sizeof($parts)-1]) ;
    
    header( "Content-type: " . $file_types[$ext] ) ;
    header( "Expires: Wed, 29 Jan 1975 04:15:00 GMT" );
    header( "Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT" );
    header( "Cache-Control: no-cache, must-revalidate" );
    header( "Pragma: no-cache" );

    print $file ;
  
  }

}