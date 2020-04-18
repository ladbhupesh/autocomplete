function getGeoCode(str) {
            if (str.length == 0) {
                document.getElementById("mylist").innerHTML = "";
                document.getElementById("mylist").style.border = "0px";
                return;
            }
            if (window.XMLHttpRequest) {
                xmlhttp = new XMLHttpRequest();
            } else {
                xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
            }
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    document.getElementById("mylist").innerHTML = this.responseText;
                }
            }
            xmlhttp.open("GET", "/coordinate-autocomplete/" + str, true);
            xmlhttp.send();
        }