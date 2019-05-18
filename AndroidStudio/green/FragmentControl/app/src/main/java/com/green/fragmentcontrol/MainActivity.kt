package com.green.fragmentcontrol

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v4.app.Fragment

class MainActivity : AppCompatActivity()
{
    private var mainFragment: MainFragment? = null
    private var menuFragment: MenuFragment = MenuFragment()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        mainFragment = supportFragmentManager.findFragmentById(R.id.fragment_main) as MainFragment
    }


    fun onFragmentChange( index: Int )
    {
        when(index)
        {
            0 -> supportFragmentManager.beginTransaction().replace(R.id.container, menuFragment ).commit()
            1 -> supportFragmentManager.beginTransaction().replace(R.id.container, mainFragment as MainFragment ).commit()
        }
    }
}
