package com.green.viewpager

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v4.app.FragmentManager
import android.support.v4.app.FragmentStatePagerAdapter
import android.support.v4.view.ViewPager
import com.green.fragmentcontrol2.Fragment1
import com.green.fragmentcontrol2.Fragment2
import com.green.fragmentcontrol2.Fragment3

class MainActivity : AppCompatActivity()
{
    var pager: ViewPager? = null

    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        pager = findViewById(R.id.pager)
        pager?.offscreenPageLimit = 3

        var adapter = MyPagerAdapter( supportFragmentManager )
        adapter.AddItem( Fragment1() )
        adapter.AddItem( Fragment2() )
        adapter.AddItem( Fragment3() )

        pager?.adapter = adapter
    }
}

class MyPagerAdapter : FragmentStatePagerAdapter
{
    private var items = mutableListOf<Fragment>()

    constructor( fm: FragmentManager ) : super( fm )
    {
    }

    fun AddItem( item: Fragment ) = items.add( item )

    override fun getItem(p: Int): Fragment = items.get(p)

    override fun getCount(): Int = items.size

}