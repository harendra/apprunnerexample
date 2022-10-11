function handle_button_press(){

    $('#results_button').click(function(){
        $.get('/test_api',function(result){
            $('#results').text(result);
        });
    });

}