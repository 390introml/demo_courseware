cs_content_header = cs_long_name = "Calendar"
cs_release_date = "2024-01-01:08:00"

queue_enable = False

cs_calendar_preview = False

cs_scripts += """<style>
.tab {
  display: flex;
  justify-content: center;
  overflow: hidden;

}

.tab button {
  background-color: inherit;
  border: none; /* Removes the border */
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  transition: 0.3s;
  font-size: 17px;
}

.tab button:hover {
  background-color: #ddd;
}

.tab button.active {
  background-color: #ccc;
}

.tabcontent {
  display: none;
  padding: 6px 12px;
  border: none; /* Removes the border */
  border-top: none;
}

.iframe-container {
            width: 100%;
            height: 100%;
            border: none;
        }
        
#googlesheet{
    width: 100%;
    height: 100%;
    border: none;
}

#Tab3 {
    /* Your new styles here */
    height: 1800px;
}
</style>"""

cs_scripts += """<script type="text/javascript">
function openTab(evt, tabName) {
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].classList.remove("active");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.classList.add("active");
}
</script>"""
