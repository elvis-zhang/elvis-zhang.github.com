h1. A simple static blog tool

Build with:
* Textile : Markup language
* Pynments : Highlight the code snippets

@your code here@

```java
public static void main(String[] args)
{
    return;
}
```



```js+php
function get()
{
    return 0;
}
```
```js+php
function get()
{
    return 0;
}
```
```java
package com.akoola.commom;

import com.akoola.R;

import android.app.Activity;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.view.Menu;
import android.view.MenuItem;

/**
 * 
 * @author larry
 *
 */
public class CommonActivity  extends Activity {
	
    /*
     * 
     */
    private BroadcastReceiver broadcastReceiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            finish();
        }
    };

    @Override
    /**
     * 
     */
    public void onResume() {
        super.onResume();
        IntentFilter filter = new IntentFilter();
        filter.addAction(Constants.ACTION_EXIT);
        this.registerReceiver(this.broadcastReceiver, filter);
    }
    
    
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.activity_main, menu);
        return true;
    }
    
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle item selection
        switch (item.getItemId()) {
            case R.id.menu_cloud:
                //showCloud();
                return true;
            case R.id.menu_suggestion:
                //showHelp();
                return true;
            case R.id.menu_about:
            	return true;
            case R.id.menu_exit:
            	
            	Intent intent = new Intent();
            	intent.setAction(Constants.ACTION_EXIT); 
            	this.sendBroadcast(intent);
            	this.finish();
            	System.exit(0);
            	
            	return true;
            
            default:
                return super.onOptionsItemSelected(item);
        }
    }
}

```
