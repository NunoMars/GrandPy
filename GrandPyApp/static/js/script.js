var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

$(window).load(function() {
  $messages.mCustomScrollbar();
  firstGrandPyMessage();
});


function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

function grandPyMessage(message) {
  $('.message.loading').remove();
  $('<div class="message new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure>' + message + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  updateScrollbar();
}

function setDate(){
  d = new Date()
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
    $('<div class="checkmark-sent-delivered">&check;</div>').appendTo($('.message:last'));
    $('<div class="checkmark-read">&check;</div>').appendTo($('.message:last'));
  }
}

function insertMessage() {
  msg = $('.message-input').val();
  if ($.trim(msg) == '') {
    return false;
  }
  escapeHtml(msg);
  $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  $('.message-input').val(null);
  updateScrollbar();
  $('<div class="message loading new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure><span></span></div>').appendTo($('.mCSB_container'));
  updateScrollbar();
  getMessageGrandPy(msg);
};

function escapeHtml(msg) {
  return msg
  .replace(/&/g, "&amp;")
  .replace(/</g, "&lt;")
  .replace(/>/g, "&gt;")
  .replace(/"/g, "&quot;")
  .replace(/'/g, "&#039;");
};

function getMessageGrandPy(msg) {
  $.ajax({
    data : {messageInput : msg},
    type : 'POST',
    url : '/process',
    dataType: "json",
    success: function(data) {
      mapGrandPyMessages(data.messages, data.position, data.tag);
    },
  });
};

var id_tags = Array();
function mapGrandPyMessages(messages, position, tag) {
  if(tag==="ups") {
    grandPyMessage(messages[0]);
    grandPyMessage(messages[1]);
    grandPyMessage(messages[2]);
    grandPyMessage(messages[3]);
  } else {
    if(id_tags.includes(tag)){
      var message_ups = "Petit coquin, a faire des blagues a PaPy.., Cherche plus haut dans la conversation je te l'ai déja trouvé!! Ha les jeuneaux...Revenons a nos moutons.. Que veux-tu que je te trouve encore?"
      grandPyMessage(message_ups);
    } else{
      id_tags.push(tag);
      grandPyMessage(messages[0]);
      grandPyMessage(messages[1]);
      grandPyMessage(messages[2]);
      $('.message.loading').remove();
      $('<div class="message new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure><div id="showMap_'+tag+'"></div></div>').appendTo($('.mCSB_container')).addClass('new');
      var elmt = document.getElementById('showMap_'+tag);
      var mq = window.matchMedia("screen and (min-width: 1024px");
      if (mq.matches) {
        elmt.style.height= "300px";
        elmt.style.width= "700px";
      } else {
        elmt.style.height= "200px";
        elmt.style.width= "260px";
      }
      initMap(position, tag);
      setDate();
      updateScrollbar();
      grandPyMessage(messages[3]);
      lastGrandPyMessage();
    };
  };
};

var tag;
var marker;
function initMap(position, tag) {
  tag = new google.maps.Map(document.getElementById('showMap_'+ tag ),{
    center: position,
    zoom: 18,
  });
  marker = new google.maps.Marker({
    position: position,
    map: tag,
  });
};

/*$('.message-submit').click(function() {
  insertMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  };
});*/
$('#message-form').submit(function(event) {
  event.preventDefault();
  insertMessage();
});
last = "Voilà petit fou! Une autre Question a me soumettre ?"
function firstGrandPyMessage() {
  if ($('.message-input').val() != '') {
    return false;
  }
  msg = "Salut coquinou, je suis GrandPy, J'aime bien"+
  " trouver des lieux mais je suis un peu rouillé"+
  " alors sois gentil avec moi,j'aime bien radoter..." +
  "mais quel lieu veux-tu que je te trouve? ZZZzzz "
  grandPyMessage(msg);
};

function lastGrandPyMessage() {
  if ($('.message-input').val() != '') {
    return false;
  }
  last = "Voilà petit fou! Une autre question à me soumettre ? Profites je suis de bonne humeur!"
  grandPyMessage(last);
};

$('.button').click(function(){
  $('.menu .items span').toggleClass('active');
  $('.menu .button').toggleClass('active');
});
