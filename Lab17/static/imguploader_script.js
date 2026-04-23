// upload image
document.querySelector('#uploadform').addEventListener('submit', function(e){
    e.preventDefault()

    const fileinput = document.querySelector('#imageinput')
    const message = document.querySelector('#message')

    if(!fileinput.files.length){
        message.textContent = "Please select an image"
        message.style.color = 'red'
        return ;
    }

    const formData = new FormData()
    formData.append('image', fileinput.files[0])

    fetch('/upload', {
        method : 'POST',
        body : formData
    })
    .then(response => response.json())
    .then(data =>{
        if(data.message){
            // show server success message
            message.textContent = data.message
            message.style.color = 'green'

            // optional: reload the page after 1s of delay
            setTimeout(()=>{location.reload()}, 1000)
        }
        else{
            message.textContent = data.error || "Upload failed"
            message.style.color = 'red'
        }
    })

})

// delete an image
function deleteimage(id){
    if(!confirm("Are you sure you want to delete this image?"))
        return;
    fetch(`/delete/${id}`, {
        method : 'DELETE',
    })
    .then(response=>response.json())
    .then(data=>{
        if(data.message){
            document.getElementById(`image-${id}.remove()`)
        }
        else{
            alert(data.error)
        }
    })
}