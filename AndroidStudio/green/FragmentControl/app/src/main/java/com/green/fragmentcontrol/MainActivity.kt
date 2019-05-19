package com.green.fragmentcontrol

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v4.app.Fragment
import android.view.Menu
import android.view.MenuItem
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast

class MainActivity : AppCompatActivity()
{
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.action_menu_bar, menu)

        val view = menu?.findItem(R.id.menu_search)?.actionView
        var editText = view?.findViewById<EditText>(R.id.editText)
        editText?.setOnEditorActionListener { v, actionId, event ->
            Toast.makeText( applicationContext, "set texts", Toast.LENGTH_SHORT ).show()
            true
        }
        return true;
    }

    override fun onOptionsItemSelected(item: MenuItem?): Boolean {

        when(item?.itemId)
        {
            R.id.refresh_action -> Toast.makeText( this, "Select Refresh Menu", Toast.LENGTH_SHORT ).show()
            //R.id.search_action ->  Toast.makeText( this, "Select Search Menu", Toast.LENGTH_SHORT ).show()
            R.id.setting_action ->  Toast.makeText( this, "Select Setting Menu", Toast.LENGTH_SHORT ).show()
            else -> Toast.makeText(this, "Invalid Action Menu Item", Toast.LENGTH_SHORT ).show()
        }

        return super.onOptionsItemSelected(item)
    }

}
