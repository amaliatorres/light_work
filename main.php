<?php
use google\appengine\api\cloud_storage\CloudStorageTools;
$bucket = ‘ '; lightwork
$root_path = 'gs://' . $bucket . '/';
$_url = 'https://console.cloud.google.com/storage/browser/lightwork';
if(isset($_POST['submit']))
{
    if(isset($_FILES['userfile']))
    {
        $name = $_FILES['userfile']['name'];
        $file_size =$_FILES['userfile']['size'];
        $file_tmp =$_FILES['userfile']['tmp_name'];
        $original = $root_path .$name;
        move_uploaded_file($file_tmp, $original);
        $_url=CloudStorageTools::getImageServingUrl($original);
    }
}

?>
    <html>

    <body>
        <form action="#" method="post" enctype="multipart/form-data"> Send these files:
            <p/> <input name="userfile" type="file" />
            <p/> <input type="submit" name="submit" value="Send files" /> </form>
    </body>

    </html>
    <?php

echo $_url;

?>
