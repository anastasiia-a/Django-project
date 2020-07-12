$(document).ready(function() {
    $('#button').on('click', function (event) {
        var text = $('#text_search').val();
        var csrftoken = $('[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: 'POST',
            data: {search: text},
            url: '/search/'+text+'/',
            beforeSend: function(xhr, settings) {xhr.setRequestHeader("X-CSRFToken", csrftoken);},
            success: function (response) {
                $(".content").html(response.html)
                history.pushState({}, 'Catalog', '/search/'+text+'/');
            }
        })
    }
)
    $('.cat').on('click', function (event) {
        event.preventDefault();
        var data = ($(this).attr('href'));
        var csrftoken = $('[name=csrfmiddlewaretoken]').val();
        $('#text').val('');

        $.ajax({
            type: 'POST',
            data: {category: data},
            url: data,
            beforeSend: function(xhr, settings) {xhr.setRequestHeader('X-CSRFToken', csrftoken);},
            success: function (response) {
                console.log(response),
                $(".content").html(response.html)
                history.pushState({}, 'Catalog', data);
                // $(this).load('index.js');
            }
        })
    })

    $('.product').on('click', function (event) {
        event.preventDefault();
        var data = ($(this).attr('href'));
        var csrftoken = $('[name=csrfmiddlewaretoken]').val();
        $('#text').val('');

        $.ajax({
            type: 'POST',
            data: {category: data},
            url: data,
            beforeSend: function(xhr, settings) {xhr.setRequestHeader('X-CSRFToken', csrftoken);},
            success: function (response) {
                $('.content').html(response.html)
                history.pushState({}, 'Сatalog', data)
            }
        })
    })
});
