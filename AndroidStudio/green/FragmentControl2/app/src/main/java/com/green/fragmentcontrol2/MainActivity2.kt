package com.green.fragmentcontrol2

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.design.widget.BottomNavigationView
import android.support.design.widget.TabLayout
import android.support.v7.widget.Toolbar
import android.util.Log
import android.view.MenuItem
import android.widget.Toast

class MainActivity2 : AppCompatActivity()
{
    val fragment1 = Fragment1()
    val fragment2 = Fragment2()
    val fragment3 = Fragment3()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2)

        supportFragmentManager?.let {
            it.beginTransaction().replace(R.id.bottom_container, fragment1 ).commit()
        }


        var navigationMenu = findViewById<BottomNavigationView>(R.id.bottom_navigation)
        navigationMenu?.setOnNavigationItemSelectedListener(object:BottomNavigationView.OnNavigationItemSelectedListener{
            override fun onNavigationItemSelected(p0: MenuItem): Boolean {
                when(p0?.itemId)
                {
                    R.id.tab1 ->
                    {
                        Toast.makeText(applicationContext, "Selected First", Toast.LENGTH_LONG).show();
                        supportFragmentManager?.beginTransaction()?.replace(R.id.bottom_container, fragment1 )?.commit()
                        return true
                    }
                    R.id.tab2 ->
                    {
                        Toast.makeText(applicationContext, "Selected Second", Toast.LENGTH_LONG).show();
                        supportFragmentManager?.beginTransaction()?.replace(R.id.bottom_container, fragment2 )?.commit()
                        return true
                    }
                    R.id.tab3 ->
                    {
                        Toast.makeText(applicationContext, "Selected Third", Toast.LENGTH_LONG).show();
                        supportFragmentManager?.beginTransaction()?.replace(R.id.bottom_container, fragment3 )?.commit()
                        return true
                    }
                    else -> Log.d("MainActivity2", "Check Error")
                }

                return false
            }
        })


//        var tab = findViewById<TabLayout>(R.id.tabs)
//        tab?.apply {
//            addTab(newTab().setText("History Call"))
//            addTab(newTab().setText("History Spam"))
//            addTab(newTab().setText("Address Call"))
//        }
//
//        tab?.addOnTabSelectedListener(object: TabLayout.OnTabSelectedListener{
//            override fun onTabSelected(p0: TabLayout.Tab?) {
//                Log.d("MainActivity", "Selected Tab : ${p0?.position ?: -1}" )
//
//                when(p0?.position)
//                {
//                    0 -> supportFragmentManager?.beginTransaction()?.replace(R.id.container, fragment1)?.commit()
//                    1 -> supportFragmentManager?.beginTransaction()?.replace(R.id.container, fragment2)?.commit()
//                    2 -> supportFragmentManager?.beginTransaction()?.replace(R.id.container, fragment3)?.commit()
//                    else -> Log.d( "Mainactivity", "Fail............")
//                }
//            }
//
//            override fun onTabReselected(p0: TabLayout.Tab?) {
//            }
//
//            override fun onTabUnselected(p0: TabLayout.Tab?) {
//            }
//        })

    }
}
