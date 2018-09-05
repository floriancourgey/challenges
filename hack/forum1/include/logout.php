<?php
unset($_SESSION['user_hack']);
session_destroy();
?>
<script>self.location.href='?'</script>