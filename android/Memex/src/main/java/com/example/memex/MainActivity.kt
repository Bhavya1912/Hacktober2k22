package com.example.memex

import android.content.Intent
import android.graphics.drawable.Drawable
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.*
import com.android.volley.Request
import com.android.volley.Response
import com.android.volley.toolbox.JsonObjectRequest
import com.bumptech.glide.Glide
import com.bumptech.glide.load.DataSource
import com.bumptech.glide.load.engine.GlideException
import com.bumptech.glide.request.RequestListener
import com.bumptech.glide.request.target.Target

class MainActivity : AppCompatActivity(), AdapterView.OnItemSelectedListener {
    private lateinit var item:String
    var currenturl:String?=null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val spinner: Spinner = findViewById(R.id.spinner)
        spinner.onItemSelectedListener = this

        // Create an ArrayAdapter using the string array and a default spinner layout
        ArrayAdapter.createFromResource(
            this,
            R.array.types,
            android.R.layout.simple_spinner_item
        ).also { adapter ->
            // Specify the layout to use when the list of choices appears
            adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
            // Apply the adapter to the spinner
            spinner.adapter = adapter
        }
    }

    override fun onItemSelected(p0: AdapterView<*>?, p1: View?, p2: Int, p3: Long) {
        item = p0?.getItemAtPosition(p2) as String


    }

    override fun onNothingSelected(p0: AdapterView<*>?) {
        TODO("Not yet implemented")
    }


    fun CallMeme(view: android.view.View) {


        val base_url="https://meme-api.herokuapp.com/gimme"
        val additive = item
        if (additive=="Cricket"){
            val final_url= "$base_url/CricketShitpost"
            CallApi(final_url)
        }
        else if(additive=="General"){
            val final_url=base_url
            CallApi(final_url)
        }
        else if(additive=="Football"){
            val final_url="$base_url/footballmemes"
            CallApi(final_url)
        }
        else if(additive=="Indian"){
            val final_url="$base_url/dankinindia"
            CallApi(final_url)
        }
        else if(additive=="Dank"){
            val final_url="$base_url/dankmemes"
            CallApi(final_url)
        }

    }
    fun CallApi( final_url:String){
        val btn:Button=findViewById(R.id.btn)
        val progress:ProgressBar=findViewById(R.id.progress_bar)
        progress.visibility=View.VISIBLE
        val image:ImageView = findViewById(R.id.image)
        val jsonObjectRequest = JsonObjectRequest(
            Request.Method.GET, final_url, null, {
                currenturl = it.getString("url")
                Glide.with(this).load(currenturl).listener(object : RequestListener<Drawable>{
                    override fun onLoadFailed(
                        e: GlideException?,
                        model: Any?,
                        target: Target<Drawable>?,
                        isFirstResource: Boolean
                    ): Boolean {
                        progress.visibility=View.GONE

                        return false
                        TODO("Not yet implemented")
                    }

                    override fun onResourceReady(
                        resource: Drawable?,
                        model: Any?,
                        target: Target<Drawable>?,
                        dataSource: DataSource?,
                        isFirstResource: Boolean
                    ): Boolean {
                        progress.visibility=View.GONE
                        image.visibility=View.VISIBLE
                        btn.text="NEXT"
                        return false
                    }
                }).into(image)
            },
            {
                Toast.makeText(this,"some error",Toast.LENGTH_SHORT).show()

            }
        )
        MySingleton.getInstance(this).addToRequestQueue(jsonObjectRequest)
    }



    fun Share(view: android.view.View) {
        val intent = Intent(Intent.ACTION_SEND)
        intent.type="text/plain"
        intent.putExtra(Intent.EXTRA_TEXT,"Look I found a nice $item meme. $currenturl")
        val chooser = Intent.createChooser(intent,"Share")
        startActivity(chooser)
    }
}