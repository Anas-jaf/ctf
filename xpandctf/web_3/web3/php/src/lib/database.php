<?php

//all mechanism started from here

class database{
    private $hostdb = "db";
    private $userdb = "root";
    private $passdb = "random_pass";
    private $namedb = "login_registration_system";
    public $pdo;

    public function __construct(){
        if(!isset($this->pdo)){
            try{
                $link = new PDO("mysql:host=".$this->hostdb.";dbname=".$this->namedb, $this->userdb, $this->passdb);
                $this->pdo = $link;
            }catch(PDOException $e){
                die("Failed to connect with database".$e->getMessage());
            }
        }
    }
}
