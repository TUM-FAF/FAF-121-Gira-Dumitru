package com.example.ide_lab_3.kakova;


import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.MotionEvent;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.app.Activity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemSelectedListener;
import android.widget.ArrayAdapter;
import android.widget.TabHost;
import android.widget.TextView;
import android.widget.Toast;
import android.view.ViewGroup;

import android.app.TabActivity;


public class MainActivity extends ActionBarActivity {

    Spinner spin1, spin2, spin3, spin4, spin5, spin6, spin7;
    Button mButton;
    EditText mEdit;
    TextView mView;
    TextView msView1, msView2, msView3, msView4, msView5, msView6, msView7;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TabHost thost = (TabHost)findViewById(R.id.tabhost);
        thost.setup();
        TabHost.TabSpec specs  = thost.newTabSpec("tg1");
        specs.setContent(R.id.Configuration);
        specs.setIndicator("New Config");
        thost.addTab(specs);

        specs  = thost.newTabSpec("tg2");
        specs.setContent(R.id.List);
        specs.setIndicator("Last config");
        thost.addTab(specs);

        specs = thost.newTabSpec("tg3");
        specs.setContent(R.id.About);
        specs.setIndicator("About");
        thost.addTab(specs);

        spin1 = (Spinner) findViewById(R.id.spinner1);
        msView1 = (TextView) findViewById(R.id.show1);
        spin1.setOnItemSelectedListener(new OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                String item = adapterView.getItemAtPosition(i).toString();
                msView1.setText(item);

            }
            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        spin2 = (Spinner) findViewById(R.id.spinner2);
        msView2 = (TextView) findViewById(R.id.show2);
        spin2.setOnItemSelectedListener(new OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                String item = adapterView.getItemAtPosition(i).toString();
                msView2.setText(item);

            }
            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        spin3 = (Spinner) findViewById(R.id.spinner3);
        msView3 = (TextView) findViewById(R.id.show3);
        spin3.setOnItemSelectedListener(new OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                String item = adapterView.getItemAtPosition(i).toString();
                msView3.setText(item);

            }
            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        spin4 = (Spinner) findViewById(R.id.spinner4);
        msView4 = (TextView) findViewById(R.id.show4);
        spin4.setOnItemSelectedListener(new OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                String item = adapterView.getItemAtPosition(i).toString();
                msView4.setText(item);

            }
            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        spin5 = (Spinner) findViewById(R.id.spinner5);
        msView5 = (TextView) findViewById(R.id.show5);
        spin5.setOnItemSelectedListener(new OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                String item = adapterView.getItemAtPosition(i).toString();
                msView5.setText(item);

            }
            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        spin6 = (Spinner) findViewById(R.id.spinner6);
        msView6 = (TextView) findViewById(R.id.show6);
        spin6.setOnItemSelectedListener(new OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                String item = adapterView.getItemAtPosition(i).toString();
                msView6.setText(item);

            }
            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        spin7 = (Spinner) findViewById(R.id.spinner7);
        msView7 = (TextView) findViewById(R.id.show7);
        spin7.setOnItemSelectedListener(new OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                String item = adapterView.getItemAtPosition(i).toString();
                msView7.setText(item);

            }
            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        mButton = (Button) findViewById(R.id.submitB);
        mEdit = (EditText) findViewById(R.id.textArea);
        mView = (TextView) findViewById(R.id.sv_name);




        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String strr = mEdit.getText().toString();
                mView.setText(strr);
                Toast.makeText(getApplicationContext(), "Configuration saved", Toast.LENGTH_LONG).show();
                mEdit.setText("");


            }
        });

    }




    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }



}
