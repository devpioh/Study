package com.green.fragmentcontrol2

import android.support.v7.app.AppCompatActivity
import android.support.v7.widget.Toolbar
import android.os.Bundle
import android.support.design.widget.TabLayout
import android.support.v4.app.Fragment
import android.util.Log

class MainActivity : AppCompatActivity() {

    val fragment1 = Fragment1()
    val fragment2 = Fragment2()
    val fragment3 = Fragment3()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val toolbar: Toolbar? = findViewById(R.id.toolbar)
        setSupportActionBar(toolbar)

        supportActionBar?.setDisplayShowTitleEnabled(false)

        supportFragmentManager?.let {
            it.beginTransaction().replace(R.id.container, fragment1 ).commit()
        }

        var tab = findViewById<TabLayout>(R.id.tabs)
        tab?.apply {
            addTab(newTab().setText("History Call"))
            addTab(newTab().setText("History Spam"))
            addTab(newTab().setText("Address Call"))
        }

        tab?.addOnTabSelectedListener(object: TabLayout.OnTabSelectedListener{
            override fun onTabSelected(p0: TabLayout.Tab?) {
                Log.d("MainActivity", "Selected Tab : ${p0?.position ?: -1}" )

                when(p0?.position)
                {
                    0 -> supportFragmentManager?.beginTransaction()?.replace(R.id.container, fragment1)?.commit()
                    1 -> supportFragmentManager?.beginTransaction()?.replace(R.id.container, fragment2)?.commit()
                    2 -> supportFragmentManager?.beginTransaction()?.replace(R.id.container, fragment3)?.commit()
                    else -> Log.d( "Mainactivity", "Fail............")
                }
            }

            override fun onTabReselected(p0: TabLayout.Tab?) {
            }

            override fun onTabUnselected(p0: TabLayout.Tab?) {
            }
        })

    }
}
