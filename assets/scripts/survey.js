function radioSelection(e) {
  $(e.target).closest('formset').find('.radio-img').each(function(img) {
    $(this).removeClass('selected');
  });

  $(e.target).prev().prop('checked', true).trigger('click');
  $(e.target).addClass('selected');
}

function checkboxSelection(e) {
  let $clickedImg = $(e.target);
  let sisterImages = $clickedImg.closest('formset').find('.checkbox-img');
  let selectedCount = 0;

  if ($clickedImg[0].classList.contains('selected')) {
    $clickedImg.removeClass('selected');
    return;
  }

  sisterImages.each(function(img) {
    if (this.classList.contains('selected')) {
      selectedCount += 1;
    }
  });

  if (selectedCount >= 3) {
    sisterImages.each(function(img) {
      $(this).removeClass('selected');
      $(this).prev().prop('checked', false);
    });
  }

  $clickedImg.addClass('selected');
}

function submitSurvey(e) {
  e.preventDefault();
  $('form').submit();
}

function bindEvents() {
  $('.radio-img').click(radioSelection);
  $('.checkbox-img').click(checkboxSelection);
  $('.submit-survey').click(submitSurvey);
}

// on DOM ready event, bind event handlers
$(function() {
  bindEvents();
});
